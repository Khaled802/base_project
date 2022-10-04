from .models import Category

def categories_processor(request):
    categories = Category.objects.all()  
    print('hi') 
    print(categories)         
    return {'categories': categories}