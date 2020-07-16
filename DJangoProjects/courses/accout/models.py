from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CourseInfo(models.Model):
	cour = [
	('Python','Python'),
	('Java','Java'),
	('.Net','.Net')]
	course = models.CharField(max_length=100,choices=cour)
	programName = models.CharField(max_length=200)
	InstructorName = models.CharField(max_length=100)
	price = models.IntegerField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
