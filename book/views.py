
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from book.forms import BookForm, BookUpdateForm
from book.models import Book
from category.models import Category


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'book/add_book.html'  
    model = Book   
    form_class = BookForm
    success_url = '/add_book/' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookListView(LoginRequiredMixin, ListView):
    template_name = 'book/list_of_books.html'
    model = Book
    context_object_name = 'all_books' 

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        number_of_books = Book.objects.count()
        context['number_of_books'] = number_of_books


        return context



def get_all_books_per_category(request, pk):

    all_books = Book.objects.filter(category_id=pk)

    return render(request, 'book/list_books_per_category.html', {'books': all_books})



class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookUpdateForm
    success_url = '/list_books/'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'book/delete_book.html'
    model = Book
    success_url = '/list_books/'

class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'book/details_book.html'
    model = Book