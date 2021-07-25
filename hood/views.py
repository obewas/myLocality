from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Neighbourhood, Photo, Business
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# # Create your views here.

# ####################### Neighbourhood Views#########################################
# def create_neighbourhood(request):
	
# 	if request.method == 'POST':
# 		form = NeighbourhoodForm(request.POST or None)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = NeighbourhoodForm()

# 	return render(request, 'create_neighbourhood.html', {'form':form})


class NeighbourhoodCreateView(LoginRequiredMixin, CreateView):
	
	model = Neighbourhood
	template_name = 'create_neighbourhood.html'
	fields = '__all__' 
	success_url = '/post-home/'

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)






# create_neigborhood()
# delete_neigborhood()
# find_neigborhood(neigborhood_id)
# update_neighborhood()
# update_occupants()



