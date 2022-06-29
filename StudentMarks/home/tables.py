from dataclasses import fields
from msilib.schema import Class
import django_tables2 as tables
from .models import StudentNames


class StudentTable(tables.Table):
   class Meta:
      model = StudentNames
      fields = ['name','email','gender','phone_number','course','reported_on']