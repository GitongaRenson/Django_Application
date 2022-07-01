from dataclasses import fields
from django import forms
from .models import StudentNames


class AddStudentForms(forms.ModelForm):
  name = forms.CharField(max_length=100,label='Enter Student Name:',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name Here'}))

  email = forms.CharField(max_length=100,label='Enter Student Email:',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student email Here'}))

  phone_number = forms.CharField(max_length=100,label='Enter Student Phone Number:',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Phone Number here'}))


  class Meta:
    model = StudentNames
    fields = ['name','email', 'gender','phone_number','course']#custom validation on django forms
    
  def clean_phone_number(self):
    phone = self.cleaned_data['phone_number']
    if len(phone) < 10:
      raise forms.ValidationError("Phone number should be 10 characters or more in length")
    if len(phone) > 13:
      raise forms.ValidationError('Phone numbers should not be more that 13 Characters in length')

   # def clean_name(self):

