
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from category.forms import CategoryForm
from category.models import Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category/create_category.html'  
    model = Category   
    form_class = CategoryForm
    success_url = '/create_category/' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories' 

    def get_queryset(self):
        return Category.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        number_of_categories = Category.objects.filter(active=True).count()
        context['number_of_categories'] = number_of_categories


        return context