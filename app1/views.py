from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("this is app 1")
def index1(request):
    return HttpResponse("this is child 1")