from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import  show_category , CreateCategory , ListCategory ,  UpdateCategory , DeleteCategory , SubscribeCategory 
# , subscribe_category , unsubscribe_category

urlpatterns = [
    path('show/<int:id>', show_category, name='category.show'),    
    path('manage/' , ListCategory.as_view() , name="categories.manage.list"),
    path('create/', CreateCategory.as_view(), name='category.manage.create'),
    path('update/<int:pk>' , UpdateCategory.as_view() , name="category.manage.update"),
    path('delete/<int:pk>' , DeleteCategory.as_view() , name="category.manage.delete"),
    path('subscribe/<int:category_id>/' , SubscribeCategory , name="category.subscribe"),
]
