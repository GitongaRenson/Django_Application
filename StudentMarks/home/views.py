import re
from urllib import request
from django.shortcuts import render
from .models import StudentNames
from .tables import StudentTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator


# Create your views here.

#This is the default root index for the application and should be accessed from the browser.

def index(request):
    calc = 45 + 20
    name = 'My name is tech'
#queryset fetchinh all the data for customernames
    student_names = StudentNames.objects.all().order_by('reported_on')

#Django tables module
    student_table = StudentTable(student_names)
    RequestConfig(request,paginate={'per_page':3}).configure(student_table)

#custom table pagination module
    paginator = Paginator(student_names,3)
    page_number = request.GET.get('page')
    paginator_module = paginator.get_page(page_number)

#Dictionary containing all the variables we want to pass and show on the HTML
    args = {'name':name,'calc':calc,'student_names':student_names,'student_table':student_table,'paginator_module':paginator_module}
    return render(request,'home/index.html',args)


