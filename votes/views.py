from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project
from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import EditProfileForm, UpdateProfileForm, UserRegisterForm, PhotoForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def create_project(request):
	
	if request.method == 'POST':
		form = ProjectForm()
		if form.is_valid():
			form.save()
	else:
		form = ProjectForm()

	return render(request, 'createproject.html', {'form':form})

def project_list(request):
	projects = Project.objects.all()

	return render(request, 'projectList.html', {'projects':projects})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('profile-edit')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file

        if edit_form.is_valid() and profile_form.is_valid():
            user_form = edit_form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profile')
    else:
        edit_form = EditProfileForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)
        args = {}
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'registration/edit_profile.html', args)


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'registration/profile.html', args)

def upload(request):
	context = dict( backend_form = PhotoForm())
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		context['posted'] = form.instance
		if form.is_valid():
			form.save()
			return redirect('/edit/')
	return render(request, 'upload.html', context)





