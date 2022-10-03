from multiprocessing import context
from turtle import title
from unicodedata import category
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy , reverse
from account.models import CustomUser
from .models import Category , Subscribe
from post.models import Post
from categories.forms import CategoryModelForm
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def show_category(request, id):
    category= Category.get_category(id)
    related_posts = Post.related_posts(category)
    is_subscribe = Subscribe.get_subscribe(category, request.user)
    return render(request, 'categories/show_category.html', context={'category': category , "related_posts":related_posts, 'subscribe': is_subscribe})

#####From Admin Page#####
class CreateCategory(SuccessMessageMixin , CreateView):
    model = Category
    fields = '__all__'
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('categories.manage.list') 
    success_message = 'Category successfully Created'
    
    extra_context = {'title': 'create category'}
    def get_context_data(self, **kwargs):
        context = super(CreateCategory, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class ListCategory(ListView):
    model = Category
    template_name = "categories/manage_categories.html"

class UpdateCategory(SuccessMessageMixin , UpdateView):
    model = Category
    template_name = 'categories/update_category.html'
    success_url =reverse_lazy('categories.manage.list')  
    success_message = 'Category successfully Updated'
    form_class = CategoryModelForm
 
class DeleteCategory(SuccessMessageMixin , DeleteView):
    model = Category
    success_url = reverse_lazy('categories.manage.list') 
    success_message = 'Category successfully Deleted'
    template_name = 'Categories/delete_category.html'

@login_required
def SubscribeCategory(request , category_id):
    selected_user = request.user
    selected_category = Category.get_category(category_id)
    selected_sub = Subscribe.get_subscribe(selected_category , selected_user)

    if(selected_sub):
        selected_sub.delete()
        return redirect(reverse('category.show', args=[category_id]))
        
    else:
        new_sub = Subscribe(category=selected_category , user=selected_user)
        new_sub.save()
        return redirect(reverse('category.show', args=[category_id]))