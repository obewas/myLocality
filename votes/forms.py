# from django import forms
# from .models import Profile, Photo, Neighbourhood, Business
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# #form creation

# class NeighbourhoodForm(forms.ModelForm):

# 	class Meta:
# 		model = Neighbourhood
# 		fields = '__all__'

# class EditProfileForm(forms.ModelForm):

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email']

# class UpdateProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = '__all__'	


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
  
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']	

# class PhotoForm(forms.ModelForm):
#   class Meta:
#       model = Photo
#       fields = ['name', 'image']


# class BusinessForm(forms.ModelForm):

# 	class Meta:
# 		model = Business
# 		fields = '__all__'

