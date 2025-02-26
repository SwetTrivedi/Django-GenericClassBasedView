from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
# Create your views here.
class Studentcreateview(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/create/'