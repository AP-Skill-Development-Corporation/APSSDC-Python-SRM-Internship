from django.forms import ModelForm
from myapp1.models import UsReg
from django import forms

class Usform(forms.ModelForm):
	class Meta:
		model = UsReg
		fields = '__all__'
		widgets = {
		"username": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"password": forms.PasswordInput(render_value=True,attrs={"class":"form-control","placeholder":"Enter Password"}),
		"salary": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Salary","min":12000,"max":50000,"step":1000,"value":12000}),
		"age": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter age","min":19,"max":100,"step":10,"value":19}),
		}


# class UsFormwd(forms.Form):
# 	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}))
# 	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
# 	salary = forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Salary","min":12000,"max":50000,"step":1000,"value":12000}))
# 	age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter age","min":19,"max":100,"step":10,"value":19}))
# 	age = forms.DateField(widget=forms.DateInput(attrs={"placeholder":"Select Date","class":"form-control datepicker"}))