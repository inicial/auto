from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'accounts/index.html')


def login_view(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        return HttpResponseRedirect("/accounts/")


def auth(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username)
        if user is not None:
            print(request.path)
            login(request, user)
    return HttpResponseRedirect("/accounts/")


def logout_view(request):
    logout(request)
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")


def registration(request):
    return render(request, r'accounts/registration.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'accounts/index.html')
