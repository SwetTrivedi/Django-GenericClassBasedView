"""
URL configuration for genericlassbasedview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
from editingview import views as v
from createview import views as v1
from updateview import views as v2
from deleteview import views as v3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.Studentlistview.as_view(),name='student'),
    path('studentlist/',views.Studentlistview1.as_view(),name='studentlist'),
    path('student/<int:id>/',views.Studentdetailview.as_view(),name='studentdetail'),
    path('student1/<int:pk>/',views.Studentdetailview1.as_view(),name='studentdetail'),

    path('contact/',v.Contactformview.as_view(),name='contact'),
    path('Thankyou/',v.thanksTemplateView.as_view(),name='thank , you'),


    # path('create/',v1.Studentcreateview.as_view(),name='stucreate'),
    # path('thanks/',v1.Thankstemplateview.as_view(),name="thankyou"),


    # path('create/',v2.Studentcreateview.as_view(),name="stucreate"),
    # path('thanks/',v2.Thankstemplate.as_view(),name="thankyou"),
    # path('update/<int:pk>',v2.Studentupdateview.as_view(),name="stuupdate"),


    
    path('create/',v3.Studentcreateview.as_view(),name="stucreate"),
    path('thanks/',v3.Thankstemplate.as_view(),name="thankyou"),
    path('update/<int:pk>',v3.Studentupdateview.as_view(),name="stuupdate"),
    path('delete/<int:pk>',v3.Studentdeleteview.as_view(),name="studelete"),

]
