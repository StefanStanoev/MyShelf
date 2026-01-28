from django.urls import path
from category import views

urlpatterns = [
    path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
    path('list_categories/', views.CategoryListView.as_view(), name='list-categories'),

]

