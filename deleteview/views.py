from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . models import Student
from .forms import Studentform
from django.views.generic.base import TemplateView

# Create your views here.
class Studentcreateview(CreateView):
    form_class=Studentform
    template_name='deleteview/student_form.html'
    success_url='/thanks/'


class Studentupdateview(UpdateView):
    model=Student
    form_class=Studentform
    template_name='deleteview/student_form.html'
    success_url='/thanks/'

class Thankstemplate(TemplateView):
    template_name='deleteview/thanks.html'

class Studentdeleteview(DeleteView):
    model=Student
    fields=['id','name','email','password']
    success_url='/create/'