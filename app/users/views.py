from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginUserForm


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
                return HttpResponseRedirect(reverse('core:index'))
    else:
        form = LoginUserForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_user(request) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

