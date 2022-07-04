import argparse
import email
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
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

#This is the default root index for the application and should be accessed from the browser.
def index(request):
   

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
    args = {'student_names':student_names,'student_table':student_table,'paginator_module':paginator_module}
    return render(request,'home/index.html',args)


@login_required(login_url='sign-in/')
def add_students(request):
    if request.method == 'POST':
        form = AddStudentForms(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            name = form.cleaned_data['name']
            form.instance.name = name.upper()
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



@login_required(login_url='sign-in/')
def update_student(request,id):
    instance = StudentNames.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,instance=instance)
        if form.is_valid():
            form_instance = form.save(commit=False)
            name = form.cleaned_data['name']
            form.instance.name = name.upper()
            form.instance.email = form.cleaned_data['email']
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




@login_required(login_url='sign-in/')
def delete_student(request,id):
    instance = StudentNames.objects.get(id=id)
    instance.delete()
    messages.add_message(request, messages.INFO, 'Student Deleted Successfully.')
    return redirect('index')




def search_student(request):
    search_keyword = request.GET['student_search']
    if search_keyword !='':
        searched_queryset = StudentNames.objects.all().filter(
        Q(name__icontains=search_keyword) |  Q(email__icontains=search_keyword) |  Q(gender__iexact=search_keyword) |  Q(phone_number__icontains=search_keyword) | Q(course__icontains=search_keyword)
        ).order_by('-reported_on')
      
         
        #custom table pagination module
        paginator = Paginator(searched_queryset,10)
        page_number = request.GET.get('page')
        paginator_module = paginator.get_page(page_number)
        args = {'paginator_module':paginator_module,'search_keyword':search_keyword}
        
        return render(request,'home/index.html',args)
    else:
        return redirect('index')
    
   
