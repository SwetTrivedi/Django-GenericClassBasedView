from django.shortcuts import render
from .forms import Contactform
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.
class Contactformview(FormView):
    template_name='school/contact.html'
    form_class=Contactform
    success_url='/Thankyou/'
    initial={'name':'swet'}
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
    

class thanksTemplateView(TemplateView):
    template_name='school/thanku.html'
    