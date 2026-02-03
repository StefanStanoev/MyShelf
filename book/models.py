from django.db import models
from category.models import Category

class Book(models.Model):
        title = models.CharField(max_length=50)
        author= models.CharField(max_length=50)
        publication_year = models.PositiveIntegerField()
        publisher = models.CharField(max_length=50)
        pages = models.PositiveIntegerField()
        genre = models.CharField(max_length=50)
        language = models.CharField(max_length=50)
        cover = models.CharField(max_length=50)
        category = models.ForeignKey(Category,on_delete=models.CASCADE, null= True, blank=True)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True) 
        updated_at = models.DateTimeField(auto_now=True)
        img = models.TextField(max_length=1000, null=True, blank=True)
        
        


        def __str__(self):
            return f'{self.title} {self.author}'