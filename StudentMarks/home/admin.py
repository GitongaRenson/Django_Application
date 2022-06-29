from django.contrib import admin
from .models import StudentNames

# Register your models here.
admin.site.site_header = 'STUDENTMARKS'
admin.site.site_title = 'Welcome TO StudenMarks Portal'
admin.site.index_title = 'Admin Portal'



class AdminCUstomerNames(admin.ModelAdmin):
  list_display = ['id','name','email','gender','course','phone_number']
  list_display_links = ['id']
  list_per_page = 5
  search_fields =['name','email','phone_number','course','gender']
  list_filter = ['gender','course']



  class Meta:
    model = StudentNames


admin.site.register(StudentNames,AdminCUstomerNames)