from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):

    """
    model for articles .
    articles has one to many relationship to users.
    
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
