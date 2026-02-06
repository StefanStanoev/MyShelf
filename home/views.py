from django.shortcuts import render
from book.models import Book

def home(request):
    context = {"book" :Book.objects.filter(best_book=True).first()}

    return render(request, 'home/homepage.html', context)
