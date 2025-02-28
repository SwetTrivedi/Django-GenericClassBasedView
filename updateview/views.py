from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from . models import Student
from django.views.generic.base import TemplateView
from django import forms
# Create your views here.
class Studentcreateview(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanks/'
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'myclass'})
        return form

class Thankstemplate(TemplateView):
    template_name='updateview/thanks.html'


class Studentupdateview(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanks/'