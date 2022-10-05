from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.contrib import messages
from post.models import Post,Like,Dislike
from django.views.generic.edit import UpdateView,CreateView
from post.views import CreatePost
from django.urls import reverse_lazy,reverse
from django.contrib.admin.views.decorators import user_passes_test
from .models import ForbiddenWord
from post.models import posts_tags, Tag
from .forms import PostModelForm, EditForbiddenWord
from django.core.mail import send_mail



# Create your views here.

def check_admin(user):
   return user.is_superuser

# show the dashboard
@user_passes_test(check_admin)
def show_dashboard(request):
    return render(request,'admn/show_dashboard.html', context={'title': 'manage dashboards'})

# list of all users 
@user_passes_test(check_admin)
def list_of_users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,'admn/list_of_users.html',context={'users':users})

# make user --> admin 
@user_passes_test(check_admin)
def be_admin(request,id):
    User = get_user_model()    
    user = User.objects.get(pk=id)
    user.is_active = True
    user.is_staff = True
    user.is_admin = True
    user.is_superuser = True
    user.save()
    messages.success(request, f'{user.username} is Admin now.')
    return redirect('list_of_users')

# block the user 
@user_passes_test(check_admin)
def block_user(request,id):
    User = get_user_model()    
    user = User.objects.get(pk=id)
    user.is_active = False
    user.is_staff = False
    user.is_admin = False
    user.is_superuser = False
    user.save()
    send_mail(
        'Blocking at Blog', #Subject
        f'Hello, {user}\n we are sorry to tell you are blocked\n for more informations you can call the admins', # Message
        'blogteam235@gmail.com', # from gmail 
        [user.email], # to gmail
        fail_silently=False,
    )
    messages.success(request,f'sent mail to {user} by blocking')
    messages.error(request, f'{user.username} is Blocked.')
    return redirect('list_of_users')

# unblock the user 
@user_passes_test(check_admin)
def unblock_user(request,id):
    User = get_user_model()    
    user = User.objects.get(pk=id)
    user.is_active = True
    user.save()
    messages.success(request, f'{user.username} is Unblocked.')
    return redirect('list_of_users')

# list of all posts
@user_passes_test(check_admin)
def list_of_posts(request):
    posts = Post.get_all_posts()
    return render(request,'admn/list_of_posts.html',context={'posts':posts})

# create post 
def create_post(request):
    if(request.POST):
        form = PostModelForm(request.POST , request.FILES)
        form.save()
        tags=request.POST["tags"].split()
        postObj=Post.get_post_by_title(request.POST["title"])
        for tag in tags:
            tagObj = Tag.get_tag(tag)
            if( not tagObj):
                tagObj=Tag()
                tagObj.name=tag
                tagObj.save()
            p=posts_tags()
            p.post=postObj
            p.tag=tagObj
            p.save()
        return redirect("list_of_posts")
    form = PostModelForm()
    return render(request , "post/create_post.html" , context={"form":form})

# delete post 
def delete_post(request,id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    messages.error(request, f'{post.title} is Deleted.')
    return redirect('list_of_posts')

# edit a post --> class-based view 
# class edit_post(UpdateView):
#     model = Post
#     fields = '__all__'
#     template_name = 'admn/edit_post.html'
#     success_url = reverse_lazy('list_of_posts')
    
#     extra_context = {'title': 'Edit post'}
#     def get_context_data(self, **kwargs):
#         context = super(UpdateView, self).get_context_data(**kwargs)
#         context.update(self.extra_context)
#         return context

# view the post 
def view_post(request, id):
    is_like =  Like.get_like(Post.get_post(id), request.user)
    is_dislike = Dislike.get_dislike(Post.get_post(id), request.user)
    return render(request, 'admn/view_post.html', context={'post': Post.get_post(id), 'like': is_like, 'dislike': is_dislike})

# control the path after like and dislike the post
def like_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login')
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
    return redirect(reverse('view_post', args=[id]))



def unlike_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login')
    else:
        Like.get_like(Post.get_post(id), request.user).delete()
    return redirect(reverse('view_post', args=[id]))


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
    return redirect(reverse('view_post', args=[id]))



def undislike_post(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'you should login')
    else:
        Dislike.get_dislike(Post.get_post(id), request.user).delete()
    return redirect(reverse('view_post', args=[id]))



class AddForbiddenWord(CreateView):
    model = ForbiddenWord
    fields = '__all__'
    template_name = 'admn/add_forbiddenword.html'
    success_url = reverse_lazy('add_forbiddenword')
    extra_context= {'forbidden_words': ForbiddenWord.objects.all(), 'update': False}



def edit_post(request, id):
    selected_post=Post.get_post(id)

    if(request.POST):
        old_posts=posts_tags.objects.filter(post=selected_post)
        old_posts.delete()

        form=PostModelForm(request.POST , request.FILES , instance=selected_post)
        form.save()

        tags=request.POST["tags"].split()
        for tag in tags:
            tagObj = Tag.get_tag(tag)
            if( not tagObj):
                tagObj=Tag()
                tagObj.name=tag
                tagObj.save()
            p=posts_tags()
            p.post=selected_post
            p.tag=tagObj
            p.save()
        return redirect("list_of_posts")

    form=PostModelForm(instance=selected_post)
    return render(request , "admn/edit_post.html" , context={"form":form})

# view the post 
def view_post(request, id):
    is_like =  Like.get_like(Post.get_post(id), request.user)
    is_dislike = Dislike.get_dislike(Post.get_post(id), request.user)
    post = Post.get_post(id)
    tags=posts_tags.get_tags(post)
    return render(request, 'admn/view_post.html', context={'post':post , "tags":tags ,'like': is_like, 'dislike': is_dislike})

def delete_forbiddenword(request, id):
    ForbiddenWord.objects.get(id=id).delete()
    return redirect(reverse('add_forbiddenword'))

def update_forbidden_words(request, id):
    if request.POST:
        print(request.POST)
        form  = EditForbiddenWord(request.POST, instance=ForbiddenWord.objects.get(id=id))
        form.save()
        form = EditForbiddenWord()
        return  render(request, 'admn/add_forbiddenword.html', context={'form': form, 'forbidden_words': ForbiddenWord.objects.all()})

    form = EditForbiddenWord(instance=ForbiddenWord.objects.get(id=id))
    return render(request, 'admn/add_forbiddenword.html', context={'form': form, 'forbidden_words': ForbiddenWord.objects.all(), 'update': True})




