from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def smith(request):
    return HttpResponse('<h1>Best test Batsman</h1>')
