from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    img = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
    