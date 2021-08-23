import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='defaultimage.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    datarticle = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50] + '...'
