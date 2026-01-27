import datetime
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
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

