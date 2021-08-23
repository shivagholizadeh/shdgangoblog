from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import auth


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            Varuser = form.save()
            login(request, Varuser)
            return redirect('AppArticlesName:PathlistName')
            # return redirect('AppAccountsName:PathLoginName')

    else:
        form = UserCreationForm()

    return render(request, '../templates/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            Varuser = form.get_user()
            login(request, Varuser)
            if 'VarNextPage' in request.POST:
                return redirect(request.POST.get('VarNextPage'))
            else:
                return redirect('AppArticlesName:PathlistName')
    else:
        form = AuthenticationForm()

    return render(request, '../templates/login.html', {'form': form})
    # return render(request, "{% url 'AppAccountsName:PathLoginName' %}", {form: form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('AppArticlesName:PathlistName')
        # return  redirect('AppProjectName:PathHomeName')
