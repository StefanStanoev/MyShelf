from django.urls import path
from category import views

urlpatterns = [
    path('add_book/', views.CategoryCreateView.as_view(), name='add-book'),
]

