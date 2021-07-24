from django.shortcuts import render
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
	posts = Post.objects.all()
	context = {
	'posts': posts
	}
	return render(request, 'posts/post_home.html', context) 

class PostListView(ListView):
	model = Post
	template_name = 'posts/post_home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'posts/post_form.html'
	fields = '__all__' 

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = '__all__'
	template_name = 'posts/post_form.html'
	

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)	 

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 	model = Post
 	success_url = 'post-home'

 	def test_func(self):
 		post = self.get_object()
 		if self.request.user == post.author:
 			return True
 		return False







