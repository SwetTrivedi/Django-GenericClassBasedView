from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class Studentlistview(ListView):
    model=Student
    # ordering=['name']

    template_name='school/student.html'
    def get_queryset(self):
        return Student.objects.filter(course='python')
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['freshers']=Student.objects.all().order_by('name')
        return context


    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name='school/superuser.html'
        elif self.request.user.is_staff:
            template_name='school/staff.html'

        else:
            template_name=self.template_name
        return[template_name]
            



# ########################################################################################################################################

# ####################################  generic diplay view #######################

from django.views.generic.detail import DetailView

class Studentdetailview(DetailView):
    model=Student
    template_name='school/student1.html'
    # context_object_name='stu'
    pk_url_kwarg='id'

##################################################################################################################################################

class Studentdetailview1(DetailView):
    model=Student
    template_name='school/student1.html'

    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args,**kwargs)
        context['all_student']=self.model.objects.all().order_by('name')
        return context

class Studentlistview1(ListView):
    model=Student




######################################################################################################################################################
########################################  create view ################################################




