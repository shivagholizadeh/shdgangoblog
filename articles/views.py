from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


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
    if request.method == 'POST':
        VarForm = forms.createarticle(request.POST, request.FILES)
        if VarForm.is_valid():
            # save article
            Varinstance = VarForm.save(commit=False)
            Varinstance.author = request.user
            Varinstance.save()
            return redirect('AppArticlesName:PathlistName')
    else:
        VarForm = forms.createarticle()

    return render(request, '../templates/articlecreate.html', {'ArticleForm': VarForm})
