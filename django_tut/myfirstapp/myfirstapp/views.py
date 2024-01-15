from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    isActive = True

    if request.method=='POST':
      clientname =   request.POST["client"]  
      check = request.POST.get('check')  #using get means no exception when no value is given
      print(clientname)
      print(check)
      if check is None : isActive = False
      else : isActive = True


    date = datetime.datetime.now()
    name='DivyaPrakash'
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascal triangle'
    ]

    students = {
        'studentName' : 'Rahul',
        'studentCollege':'zyz',
        'studentCity' : 'lucknow'
    }

    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':students
    }

    
    # return HttpResponse('<h1>Hello</h1>'+str(date))
    return render(request,"home.html",data)

def about(request):
    print("this is a about function")
    # return HttpResponse('<h1>This is a about page of my first app</h1>')
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse('<h1>This is a services page of my first app</h1>')
    return render(request,"services.html",{})