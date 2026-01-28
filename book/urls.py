from django.urls import path
from book import views

urlpatterns = [
    path('add_book/', views.BookCreateView.as_view(), name='add-book'),
    path('list_books/', views.BookListView.as_view(), name='list-books'),
]