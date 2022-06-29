import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    calc = 45 + 20
    name = 'My name is tech'
    return render(request,'home/index.html',{'name':name,'calc':calc})