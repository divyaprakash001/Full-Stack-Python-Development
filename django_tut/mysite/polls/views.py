from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
# from django.template import loader
from .models import Question,Choice
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context = {'questions':latest_question_list}
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
    
'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404('Question does not exist.')

    context = {'questions':question}
    return render(request,'polls/detail.html',context)
'''

def detail(request, question_id):
  
    question = get_object_or_404(Question,pk=question_id)
    
    context = {'question':question}
    return render(request,'polls/detail.html',context)


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context =  {
                "question": question,
                "error_message": "You didn't select a choice.",
            }
        render(request,"polls/detail.html",context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})