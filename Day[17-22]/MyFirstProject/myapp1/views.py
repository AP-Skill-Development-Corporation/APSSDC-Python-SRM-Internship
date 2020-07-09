from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
	return HttpResponse("Hi Welcome Raju")

def home(request):
	return render(request,'myapp1/index.html')
	
def home1(request,name):
	return render(request,'myapp1/abt.html',{'na':name})

def excr(request):
	return render(request,'myapp1/cnt.html')

def jsrt(request):
	return render(request,'myapp1/javascript.html')

def reg(request):
	return render(request,'myapp1/register.html')

def regi(request):
	return render(request,'myapp1/botregi.html')

def rgform(request):
	if request.method == "POST":
		usname = request.POST['uname']
		pswd = request.POST['pwd']
		gdr = request.POST['gender']
		language = request.POST['lang']
		message = request.POST['msg']
		dt = {'un':usname,'pd':pswd,'gd':gdr,'lag':language,'mg':message}
		return render(request,'myapp1/display.html',{'ft':dt})
	return render(request,'myapp1/registerform.html')

def lg(request):
	if request.method == "POST":
		if request.POST['uname'] == 'raju' and request.POST['psd'] == '123':
			return render(request,'myapp1/welcome.html',{'name':'raju'})
		return HttpResponse("Invalid Username or Password")	
	return render(request,'myapp1/login.html')