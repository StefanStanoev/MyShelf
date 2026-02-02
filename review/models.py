from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Review(models.Model):
       book = models.ForeignKey(Book, on_delete=models.CASCADE)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       rating = models.PositiveIntegerField(choices=[(i,i) for i in range(1,6)])
       comment = models.TextField(blank=True)

       def __str__(self):
           return f"{self.user} rated the book {self.book} {self.rating} stars"

