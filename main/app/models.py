from email.policy import default
from tkinter import CASCADE
from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class UserModel(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class uploadedFile(models.Model):
    file = models.FileField(upload_to = 'media')
    

class resultResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    result_tags = models.TextField(null=True)
    product_list = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)