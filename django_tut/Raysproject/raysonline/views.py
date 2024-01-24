from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse('<h1>This is the home page</h1>')

def contactus(request):
    return HttpResponse('<h1>This is the contact page</h1>')
