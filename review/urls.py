from django.urls import path
from review import views

urlpatterns = [
    path('add_review/<int:book_id>/', views.add_review, name='add-review'),

]