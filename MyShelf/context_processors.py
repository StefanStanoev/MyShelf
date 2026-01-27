from category.models import Category

def get_active_categories(request):
    return {'categories': Category.objects.filter(active=True)}