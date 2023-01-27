from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Animal(models.Model):
    title = models.CharField(max_length=256)
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")
    image_url = models.URLField(default="https://wildcard.codestuff.io/cat/250/250")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('animal_detail', args=[str(self.id)])
