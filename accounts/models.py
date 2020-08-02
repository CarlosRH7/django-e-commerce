from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

	telefono=models.CharField(max_length=140,blank=True,null=True)
	desc=models.TextField(blank=True,null=True)
	img=models.ImageField(blank=True,null=True)
	usuario=models.OneToOneField(User)

	def __str__(self):
		return "El perfil del usuario{}".format(self.usuario)