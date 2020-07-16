from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accout.models import CourseInfo

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']

class CourseInfoForm(ModelForm):
	class Meta:
		model = CourseInfo
		fields = ['course','programName','InstructorName','price']