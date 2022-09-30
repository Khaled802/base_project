from multiprocessing import context
from turtle import title
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('post.show_all')
    
    extra_context = {'title': 'create post'}
    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    
def show_all_posts(request):
    context = {'title': 'Posts', 'posts': Post.get_all_posts()}
    return render(request, 'post/show_all_posts.html', context=context)

def show_post(request, id):
    return render(request, 'post/show_post.html', context={'post': Post.get_post(id)})
