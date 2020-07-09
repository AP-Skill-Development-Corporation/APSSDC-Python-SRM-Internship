"""MyFirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name="HI"),
    path('sample/',views.home,name="hom1"),
    path('sample1/<str:name>/',views.home1,name="hm1"),
    path('extcss/',views.excr,name="extncss"),
    path('jscp/',views.jsrt,name="jc"),
    path('register/',views.reg,name="rg"),
    path('botreg/',views.regi,name="regis"),
    path('regform/',views.rgform,name="regf"),
    path('login/',views.lg,name="log"),
]
