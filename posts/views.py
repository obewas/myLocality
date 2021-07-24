from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
	posts = Post.objects.all()
	context = {
	'posts': posts
	}
	return render(request, 'post_home.html', context) 

class PostListView(ListView):
	model = Post
	template_name = 'post_home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'