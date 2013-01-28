# Create your views here.
from django.shortcuts import render

from Smartility.apps.categories.models import Category

def index(request):
    context={}
    categories = Category.objects.all()
    context.update({'categories':categories})
    return render(request,'master.djhtml',context)

def facebook_channel(request):
    return render(request,'facebook_channel.html')