from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return redirect(watchshop_home)


@login_required(login_url='/watchshop/sign-in/')
def watchshop_home(request):
    return render(request, 'watchshop/home.html', {})


def watchshop_sign_up(request):
    return render(request, 'watchshop/sign_up.html', {})

