#blog/views.py
from django.views.generic import ListView

from .models import Post

#from django.shortcuts import render

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'