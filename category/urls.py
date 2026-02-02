from django.urls import path
from category import views

urlpatterns = [
    path('create_category/', views.CategoryCreateView.as_view(), name='create-category'),
    path('list_categories/', views.CategoryListView.as_view(), name='list-categories'),
    path('delete_category/', views.CategoryDeleteSelectView.as_view(),name='delete-category-select'),
    path('delete_category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete-category'),

]

