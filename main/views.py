from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')

    else:
        form = UserForm()
        return render(request, 'user/add_user.html', {'form': form})


def signin(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect(request, 'index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 하세요')

    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})


def logout(request):
    logout(request)
