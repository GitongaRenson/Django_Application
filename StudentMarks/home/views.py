import re
from urllib import request
from django.shortcuts import render
from .models import StudentNames
from .tables import StudentTable
from django_tables2 import RequestConfig


# Create your views here.

#This is the default root index for the application and should be accessed from the browser.

def index(request):
    calc = 45 + 20
    name = 'My name is tech'

    student_names = StudentNames.objects.all()
    student_table = StudentTable(student_names)
    RequestConfig(request,paginate={'per_page':3}).configure(student_table)
    args = {'name':name,'calc':calc,'student_names':student_names,'student_table':student_table}
    return render(request,'home/index.html',args)


