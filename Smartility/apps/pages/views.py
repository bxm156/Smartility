# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,'master.djhtml')

def facebook_channel(request):
    return render(request,'facebook_channel.html')