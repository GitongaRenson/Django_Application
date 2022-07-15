from django.conf.urls import url, include
from . import views


urlpatterns = [
url(r'^simulate-adding-students/',views.simulate_adding_students,name='simulate_adding_students'), 
  
 url(r'^students/',views.StudentsView.as_view(),name='get_create_students'), 
 url(r'^fetch-quote/',views.fetch_quote,name='fetch_quote'),
 url(r'^update-students/(?P<id>[\w-]+)/$',views.StudentsUpdateView.as_view(),name='update_delete_students'), 

 url(r'^add-students/',views.add_students,name='add_students'), 
 url(r'^update-student/(?P<id>[\w-]+)/$',views.update_student,name='update_student'),
 url(r'^delete-students/(?P<id>[\w-]+)/$',views.delete_student,name='delete_student'),
 url(r'^search-student/',views.search_student,name='search_student'), 
 url(r'^',views.index,name='index'),
 
]

#This is the url config for the home application. This is where all the views are connected to the url