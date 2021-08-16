from django.db import models


# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(default='defaultimage.jpg',blank=True)

    # author =

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50] + '...'
