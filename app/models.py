from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100, default=None)
    image_url = models.URLField(blank=True)
    description = models.TextField(default=None)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Only user who created can edit/delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
