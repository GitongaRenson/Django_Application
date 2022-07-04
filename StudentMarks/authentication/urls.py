from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^sign-out/',views.sign_out,name='sign_out'),
  url(r'^sign-in/',views.sign_in,name='sign_in'),
  url(r'^register-user/',views.register_user,name='register_user')

]

#this is the url config for the authentication application. This is where all the views are connected to the url.py file
