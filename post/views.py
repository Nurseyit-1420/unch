from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.db.models import Q
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)


class PostListViev(ListView):
    model=Post
    template_name = 'post/post_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(tittle__icontains=query)|
                Q(author__username__icontains=query)
            ) 
        return qs


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context