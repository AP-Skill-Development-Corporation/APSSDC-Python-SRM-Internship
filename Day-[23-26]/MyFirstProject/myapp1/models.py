from django.db import models

# Create your models here.

class UsReg(models.Model):
	username = models.CharField(max_length=150)
	password = models.CharField(max_length=50)
	salary = models.FloatField()
	age = models.IntegerField()
	imgup = models.ImageField(upload_to="document/",null=True)

	def __str__(self):
		return self.username+" "+str(self.age)

