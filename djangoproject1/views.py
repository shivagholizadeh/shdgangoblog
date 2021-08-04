from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request) :
    # return  HttpResponse('Hi , hello world')
     return render(request,'about.html')


def home(request):
    # return  HttpResponse('hi home')
    return  render(request,'home.html')


