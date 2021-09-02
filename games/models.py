from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default='')
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games-detail', args=[str(self.id)])