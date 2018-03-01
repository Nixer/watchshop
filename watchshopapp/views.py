from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from watchshopapp.forms import UserForm, WatchShopForm, UserFormForEdit, WatchForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from watchshopapp.models import Watch

# Create your views here.
def home(request):
    return redirect(watchshop_home)


@login_required(login_url='/watchshop/sign-in/')
def watchshop_home(request):
    return redirect(watchshop_watch)


@login_required(login_url='/watchshop/account/')
def watchshop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    watchshop_form = WatchShopForm(instance=request.user.watchshop)

    if request.method == 'POST':
        user_form = UserFormForEdit(request.POST, instance=request.user)
        watchshop_form = WatchShopForm(request.POST, request.FILES, instance=request.user.watchshop)

        if user_form.is_valid() and watchshop_form.is_valid():
            user_form.save()
            watchshop_form.save()

    return render(request, 'watchshop/account.html', {
        'user_form': user_form,
        'watchshop_form': watchshop_form
    })


@login_required(login_url='/watchshop/watch/')
def watchshop_watch(request):
    watches = Watch.objects.filter(watchshop=request.user.watchshop).order_by("-id")
    return render(request, 'watchshop/watch.html', {
        "watches": watches
    })


@login_required(login_url='/watchshop/watch/')
def watchshop_add_watch(request):
    form = WatchForm()
    if request.method == "POST":
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)
            watch.watchshop = request.user.watchshop
            watch.save()
            return redirect(watchshop_watch)

    return render(request, 'watchshop/add_watch.html', {
        'form': form
    })

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

