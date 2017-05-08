from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'

