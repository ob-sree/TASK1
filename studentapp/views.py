from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(response):
    return HttpResponse('<h1>Hello Welcome to Student Portal</h1>')

def about(respnse):
    return HttpResponse('<h1> About page</h1>')