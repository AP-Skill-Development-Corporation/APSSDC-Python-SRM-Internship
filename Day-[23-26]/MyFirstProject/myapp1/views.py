from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp1.models import UsReg
from myapp1.forms import Usform
from MyFirstProject import settings
from django.core.mail import send_mail
from django.contrib import messages
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

def showall(request):
	d = UsReg.objects.all()
	return render(request,'myapp1/showall.html',{'r':d})

def userreg(request):
	if request.method == "POST":
		l = Usform(request.POST,request.FILES)
		if l.is_valid():
			l.save()
			return HttpResponse("User Data is saved Successfully")
	p = Usform()
	return render(request,'myapp1/userrg.html',{'usg':p})

def usvwe(request,pk):
	r = UsReg.objects.get(id=pk)
	return render(request,'myapp1/usview.html',{'data':r})

def dlt(request,kl):
	t = UsReg.objects.get(id=kl)
	t.delete()
	return HttpResponse("User deleted Successfully")

def upsr(request,pl):
	fg = UsReg.objects.get(id=pl)
	if request.method == "POST":
		ft = Usform(request.POST,request.FILES,instance=fg)
		if ft.is_valid():
			ft.save()
			return redirect('/showall')
	ft = Usform(instance=fg)
	return render(request,'myapp1/userrg.html',{'usg':ft})

def cntform(request):
	if request.method == "POST":
		rec = request.POST['rcv']
		subj = request.POST['sub']
		mess = request.POST['msg']
		sd = settings.EMAIL_HOST_USER
		snd = send_mail(subj,mess,sd,[rec])
		if snd == 1:
			messages.warning(request,"Mail has been sent successfully")
			return redirect('/cnt')
		return HttpResponse("Mail didn't sent")
	return render(request,'myapp1/contact.html')
