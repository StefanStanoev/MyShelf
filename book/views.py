import datetime
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from book.forms import BookForm
from book.models import Book


class BookCreateView(CreateView):
    template_name = 'book/add_book.html'
    model = Book
    form_class = BookForm
    success_url = '/list_of_books/' 
    permission_required = 'book.add_book'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = datetime.datetime.now()
        context['current_datetime'] = now

        active_books = Book.objects.filter(active=True)
        context['active_books'] = active_books

        return context
    
    