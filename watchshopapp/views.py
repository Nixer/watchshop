from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from watchshopapp.forms import  UserForm, WatchShopForm


# Create your views here.
def home(request):
    return redirect(watchshop_home)


@login_required(login_url='/watchshop/sign-in/')
def watchshop_home(request):
    return render(request, 'watchshop/home.html', {})


def watchshop_sign_up(request):
    user_form = UserForm()
    watchshop_form = WatchShopForm()
    return render(request, 'watchshop/sign_up.html', {
        'user_form': user_form,
        'watchshop_form': watchshop_form
    })

