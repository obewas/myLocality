from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Neighbourhood, Photo, Business
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# # Create your views here.

# ####################### Neighbourhood Views#########################################
class NeighbourhoodCreateView(LoginRequiredMixin, CreateView):
	
	model = Neighbourhood
	template_name = 'create_neighbourhood.html'
	fields = '__all__' 
	success_url = '/post-home/'

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)


class NeighbourhoodListView(ListView):
	model = Neighbourhood
	template_name = 'neighbourhood_list.html'
	context_object_name = 'hoods'
	


class NeighbourhoodDetailView(DetailView):
	model = Neighbourhood
	template_name = 'hood_detail.html'



class NeighbourhoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Neighbourhood
	fields = '__all__'
	template_name = 'hood_form.html'
	
	def test_func(self):
		obj = self.get_object()
		if obj.admin == self.request.user:
			return True
		return False

class NeighbourhoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 	model = Neighbourhood
 	success_url = 'post-home'

 	def test_func(self):
 		hood = self.get_object()
 		if self.request.user == hood.admin:
 			return True
 		return False
def update_occupants():
	pass
################################### Business Views ##############################################################################

class BusinessCreateView(LoginRequiredMixin, CreateView):
	
	model = Business
	template_name = 'business/create_business.html'
	fields = '__all__' 
	success_url = '/post-home/'

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

class BusinessListView(ListView):
	model = Business
	template_name = 'business/business_list.html'
	context_object_name = 'businesses'
	


class BusinessDetailView(DetailView):
	model = Business
	template_name = 'business/business_detail.html'



class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Business
	fields = '__all__'
	template_name = 'business/business_update.html'
	
	def test_func(self):
		obj = self.get_object()
		if obj.user== self.request.user:
			return True
		return False

class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 	model = Neighbourhood
 	success_url = 'post-home'

 	def test_func(self):
 		obj = self.get_object()
 		if obj.user == self.request.user:
 			return True
 		return False

def search_business(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Business.objects.filter(name__contains=query_name)
            return render(request, 'business/business_search.html', {"results":results})

    return render(request, 'business/business_search.html')





