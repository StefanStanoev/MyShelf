import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from book.forms import BookForm
from book.models import Book


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'book/add_book.html'  
    model = Book   
    form_class = BookForm
    success_url = '/add_book/' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

