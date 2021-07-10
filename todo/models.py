from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
# Create your models here
from datetime import date 
class works(models.Model):
	work 			=models.CharField(max_length=1000)
	Description		=models.CharField(max_length=1000,null=True,blank=True)
	DeadLine		=models.DateField(null=True,blank=True)
	user    		=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

	def __str__(self):
		return f"{self.work}"