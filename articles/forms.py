from django import forms
from . import models


class createarticle(forms.ModelForm):
    class Meta:
        model = models.article
        fields = ['title', 'slug', 'body', 'image','datarticle']
