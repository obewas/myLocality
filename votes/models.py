from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
# Create your models here.

class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	full_name = models.CharField(max_length=100, default='')
# 	estate = models.CharField(max_length=100, default='')
# 	city = models.CharField(max_length=100, default='')
# 	contact = models.CharField(default='', max_length=200)
# 	phoneNumber = models.IntegerField(default=0)
# 	image = models.ForeignKey(Photo, on_delete=models.CASCADE,null=True, blank=True)
# 	profession = models.CharField(max_length=200)

# 	def __str__(self):

# 		return f'{self.user.username} Profile'


# class Neighbourhood(models.Model):
#  	name = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
#  	occupants_count = models.IntegerField(null=True)
 	

#  	def __str__(self):
#  		return str(self.name)


# class Business(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
# 	neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
# 	email = models.CharField(max_length=200)
# 	industry = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name






