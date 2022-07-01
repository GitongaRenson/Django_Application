import argparse
import re
from urllib import request
from django.shortcuts import redirect, render
from .models import StudentNames
from .tables import StudentTable
from django_tables2 import RequestConfig
from django.core.paginator import Paginator
from .forms import AddStudentForms, UpdateStudentForm
from django.template.context_processors import csrf
from django.contrib import messages

# Create your views here.

#This is the default root index for the application and should be accessed from the browser.

def index(request):
    calc = 45 + 20
    name = 'My name is tech'
#queryset fetchinh all the data for customernames
    student_names = StudentNames.objects.all().order_by('-reported_on')

#Django tables module
    student_table = StudentTable(student_names)
    RequestConfig(request,paginate={'per_page':3}).configure(student_table)

#custom table pagination module
    paginator = Paginator(student_names,10)
    page_number = request.GET.get('page')
    paginator_module = paginator.get_page(page_number)

#Dictionary containing all the variables we want to pass and show on the HTML
    args = {'name':name,'calc':calc,'student_names':student_names,'student_table':student_table,'paginator_module':paginator_module}
    return render(request,'home/index.html',args)

def add_students(request):
    if request.method == 'POST':
        form = AddStudentForms(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Data added Successfully.')
            return redirect('index')
        else:
            args = {'form':form}
            return render(request,'home/add-student.html',args)
    else:
        form = AddStudentForms()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'home/add-student.html',args)

def update_student(request,id):
    instance = StudentNames.objects.get(id=id)
    print(instance)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,instance=instance)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form.instance.name = form.cleaned_data['name']
            form.instance.email = form.cleaned_data['email']
            form.instance.gender = form.cleaned_data['gender']
            form.instance.phone_number = form.cleaned_data['phone_number']
            form.instance.course = form.cleaned_data['course']
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully.')
            return redirect('index')

        else:
            args = {'form':form}
            return render(request, 'home/update-student.html',args)
    else:
        form = UpdateStudentForm(instance=instance)
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'home/update-student.html',args)




