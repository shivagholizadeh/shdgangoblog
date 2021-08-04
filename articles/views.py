from django.shortcuts import render

# Create your views here.
from . import models


def articles_list(request):
    varArticlesObject = models.article.objects.all().order_by('date')

    # 1   return render(request, '../templates/articlelist.html')
    # 2  return render(request, '../templates/articlelist.html', {'articles': articles})
    varArticleList = {'articles': varArticlesObject}
    return render(request, '../templates/articlelist.html', varArticleList)
