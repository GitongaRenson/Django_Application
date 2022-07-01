from django.conf.urls import url, include
from . import views


urlpatterns = [
 url(r'^add-students',views.add_students,name='add_students'), 
 url(r'^',views.index,name='index'),
 
]

#This is the url config for the home application. This is where all the views are connected to the url