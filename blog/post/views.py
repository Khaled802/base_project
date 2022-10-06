
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from .models import Post, Like, Dislike, Comment, Tag, posts_tags
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CommentForm
from admn.models import ForbiddenWord
from categories.models import Category, Subscribe
from django.http.request import HttpRequest



# Create your views here.
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'details', 'picture','category']
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('post.show_all')
    
    extra_context = {'title': 'create post'}
    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    
def show_all_posts(request):
    if request.user.is_anonymous!= True:
        posts=[]
        list_of_categories=Category.objects.all()
        for cat in list_of_categories:
            if Subscribe.get_subscribe(cat,request.user):
                posts+=(list(Post.objects.filter(category=cat)))
        if posts==[]:
            mydata =update_likes() 
            context = {'title': 'Posts', 'posts': mydata}
            return render(request, 'post/show_all_posts.html', context=context)
        else:
            update_likes()
            posts = Post.objects.filter(id__in=[o.id for o in posts]).order_by("-num_of_likes","-created_time")[:5]
            # posts=list_to_queryset(posts)
            context = {'title': 'Posts', 'posts': posts}
            return render(request, 'post/show_all_posts.html', context=context)
    else:
        mydata = update_likes() 
        context = {'title': 'Posts', 'posts': mydata}
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
    tags = posts_tags.get_tags(Post.get_post(id))
    context = {'post': Post.get_post(id), 'form': form, 'like': is_like, 'dislike': is_dislike, 'comments':comments, 
    'dislikes_num': Dislike.get_post_dislikes(id), 'likes_num': Like.get_post_likes(id), 'forbidden_words':ForbiddenWord.get_all(),
    'tags': tags }
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



def update_likes():
    posts=Post.objects.all() 
    for post in posts : 
        post.num_of_likes=Like.get_post_likes(post.id) 
        post.save() 
    mydata = Post.objects.order_by("-num_of_likes","created_time")[:5]
    return mydata



def search(request):
    context={}
    print(request.GET)
    if(request.GET):
        if(request.GET["post_title"]):
            passed_title = request.GET["post_title"]
            titled_post= Post.get_post_by_title(passed_title)
            context["titled_post"]=titled_post

        if(request.GET["post_tag"]):
            passed_tag = request.GET["post_tag"]
            tagged_posts= posts_tags.get_posts(passed_tag)
            context["tagged_posts"]=tagged_posts
        print('context', context)
        return render(request ,'post/search.html' , context)

    context = {'title': 'Posts'}
    return render(request, 'post/search.html', context=context)



def view_tag(request, tag):
    new_request = HttpRequest()
    new_request.GET['post_tag'] = tag
    new_request.GET['post_title'] = None
    return search(new_request)
