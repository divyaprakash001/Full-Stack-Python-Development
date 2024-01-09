from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):
    date = datetime.datetime.now()
    print("test function called from view")
    # return HttpResponse('<h1>Hello</h1>'+str(date))
    return render(request,"home.html",{})

def about(request):
    print("this is a about function")
    # return HttpResponse('<h1>This is a about page of my first app</h1>')
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse('<h1>This is a services page of my first app</h1>')
    return render(request,"services.html",{})