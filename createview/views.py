from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
# Create your views here.
class Studentcreateview(CreateView):
    model=Student
    fields=['name','email','password']
    # success_url='/create/'
    success_url='/thanks/'

class Thankstemplateview(TemplateView):
    template_name='createview/thanks.html'
