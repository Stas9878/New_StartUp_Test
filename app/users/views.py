from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import LoginUserForm, RegisterUserForm


def register_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'users/login.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, 
                username=cd['username'], 
                password=cd['password']
            )

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('links:index'))
    else:
        form = LoginUserForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_user(request) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile_user(request) -> HttpResponse:
    links_list = request.user.links.all()
    return render(request, 'users/profile.html', {
        'user': request.user,
        'links': links_list
    })
