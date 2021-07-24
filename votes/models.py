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


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	contact = models.CharField(default='', max_length=200)
	phoneNumber = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_image' , blank=True)
	profession = models.CharField(max_length=200)

	def __str__(self):

		return f'{self.user.username} Profile'


	def createProfile(sender, **kwargs):
		if kwargs['created']:
			user_profile = Profile.objects.created(user=kwargs['instance'])
			post_save.connect(createProfile, sender=User)


class Project(models.Model):
	title = models.CharField(max_length=200, null=True)
	description = models.TextField()
	posted_by = models.CharField(max_length=200, null=True)
	image = models.ImageField(upload_to='images', null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.title



