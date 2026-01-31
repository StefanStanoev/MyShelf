from django.urls import path
from book import views

urlpatterns = [
    path('add_book/', views.BookCreateView.as_view(), name='add-book'),
    path('list_books/', views.BookListView.as_view(), name='list-books'),
    path('list_books_per_category/<int:pk>/',views.get_all_books_per_category,name= 'list-books-per-category'),
    path('update_book/<int:pk>/',views.BookUpdateView.as_view(),name= 'update-book'),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name='delete-book'),
    path('details_book/<int:pk>/', views.BookDetailView.as_view(), name='details-book'),
]