from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hi(request):
	return HttpResponse('Hi badulla,Welcome to DJango session')

def hello(request):
	return HttpResponse('<h1 style="color:blue;"><center>Hello badulla,Welcome to Django session organized by APSSDC</center></h1>')

def hi1(request,val):
	return HttpResponse('<h1>hi '+val+'Welcome to DJango session</h1>')

def rollno(request,num):
	return HttpResponse('<h1>Hi,this is ur rollno '+str(num)+'</h1>')

def details(request,name,rollno):
	return HttpResponse("Hi "+name+" this is ur rollno "+str(rollno))