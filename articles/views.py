from django.shortcuts import render,HttpResponse
from . import models
from django.contrib.auth.decorators import  login_required

def articles_list(request):
    varArticlesObject = models.article.objects.all().order_by('-date')
    varArticleList = {'VarTableArticle': varArticlesObject}
    return render(request, '../templates/articlelist.html', varArticleList)


def articles_detail(request, ParamSlug):
    varArticlesObject = models.article.objects.get(slug=ParamSlug)
    # varArticleList  = {'VarTableArticle': varArticlesObject}
    return render(request, '../templates/articledetail.html', {'VarTableArticle': varArticlesObject})

@login_required(login_url='/accounts/login')
def articles_create(request):
    return render(request, '../templates/articlecreate.html')
