from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from watchshopapp.forms import UserForm, WatchShopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return redirect(watchshop_home)


@login_required(login_url='/watchshop/sign-in/')
def watchshop_home(request):
    return render(request, 'watchshop/home.html', {})


@login_required(login_url='/watchshop/account/')
def watchshop_account(request):
    return render(request, 'watchshop/account.html', {})


@login_required(login_url='/watchshop/watch/')
def watchshop_watch(request):
    return render(request, 'watchshop/watch.html', {})


def watchshop_sign_up(request):
    user_form = UserForm()
    watchshop_form = WatchShopForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        watchshop_form = WatchShopForm(request.POST, request.FILES)

        if user_form.is_valid() and watchshop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_watchshop = watchshop_form.save(commit=False)
            new_watchshop.owner = new_user
            new_watchshop.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            ))

            return redirect(watchshop_home)


    return render(request, 'watchshop/sign_up.html', {
        'user_form': user_form,
        'watchshop_form': watchshop_form
    })

