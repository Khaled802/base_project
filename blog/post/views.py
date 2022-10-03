from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from .models import Post, Like, Dislike, Comment
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CommentForm
from admn.models import ForbiddenWord


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
    if request.POST:
        if request.user.is_anonymous:
            messages.warning(request, 'you should login to write a comment')
        else:
            new_comment = Comment()
            new_comment.user = request.user
            new_comment.post = Post.get_post(id)
            new_comment.comment_text = request.POST['comment_text']
            new_comment.save()
        return redirect(reverse('post.show', args=[id]))


    is_like =  Like.get_like(Post.get_post(id), request.user)
    is_dislike = Dislike.get_dislike(Post.get_post(id), request.user)
    comments = Comment.objects.filter( post=Post.get_post(id))
    form = CommentForm()
    context = {'post': Post.get_post(id), 'form': form, 'like': is_like, 'dislike': is_dislike, 'comments':comments, 
    'dislikes_num': Dislike.get_post_dislikes(id), 'likes_num': Like.get_post_likes(id), 'forbidden_words':ForbiddenWord.get_all() }
    return render(request, 'post/show_post.html', context=context)

def like_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login to like')
    else:
        new_like = Like()
        user = request.user
        post = Post.get_post(id)
        new_like.user = user
        new_like.post = post
        new_like.save()
        dislike = Dislike.get_dislike(post, user)
        if dislike:
            dislike.delete()
    return redirect(reverse('post.show', args=[id]))



def unlike_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login to dislike')
    else:
        Like.get_like(Post.get_post(id), request.user).delete()
    return redirect(reverse('post.show', args=[id]))


def dislike_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login')
    else:
        new_dislike = Dislike()
        user = request.user
        post = Post.get_post(id)
        new_dislike.user = user
        new_dislike.post = post
        new_dislike.save()
        like = Like.get_like(post, user)
        if like:
            like.delete()
    return redirect(reverse('post.show', args=[id]))



def undislike_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login')
    else:
        Dislike.get_dislike(Post.get_post(id), request.user).delete()
    return redirect(reverse('post.show', args=[id]))