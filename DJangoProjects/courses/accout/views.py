from django.shortcuts import render,redirect
from django.http import HttpResponse
from accout.forms import UserSignupForm, CourseInfoForm
from django.contrib.auth.decorators import login_required
from accout.models import CourseInfo
# Create your views here.

def msg(request):
	return HttpResponse('hi i am here')

def signUp(request):
	if request.method=='POST':
		form = UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('<script>alert("User Data inserted successfully")</script>')
	form = UserSignupForm()
	return render(request,'accout/signUp.html',{'form':form})

@login_required
def home(request):
	return render(request,'accout/home.html',{})

@login_required
def addCourse(request):
	if request.method=='POST':
		form = CourseInfoForm(request.POST)
		if form.is_valid():
			fr = form.save(commit=False)
			fr.user_id = request.user.id
			fr.save()
			return redirect('home')

	form = CourseInfoForm()
	return render(request,'accout/addCourse.html',{'form':form})

@login_required
def showCorseInfo(request):
	data = CourseInfo.objects.filter(user_id=request.user.id)
	return render(request,'accout/showCorseInfo.html',{'data':data})








