from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from users.models import Profile
# Create your models here.

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Neighbourhood(models.Model):
    name = models.CharField(max_length=200, null=True)
    estate = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    occupants_count = models.IntegerField(null=True)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
 	

    def __str__(self):
        return str(self.name)


class Business(models.Model):
	name = models.CharField(max_length=150, null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
	email = models.EmailField()
	industry = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name






