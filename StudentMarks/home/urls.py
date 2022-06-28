from django.conf.urls import url, include
from home import views
from . import views


urlpatterns = [
  url(r'^',views.index,name='index'),
]