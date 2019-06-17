from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#比较灵活
#     return HttpResponse('hello')

def home(request):
    return render(request,'home.html')