from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm, RegisterUserForm


def register_user(request) -> HttpResponse:
    '''Роутер для регистрации юзеров'''
    
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
    '''Роутер для аутентификации юзеров'''

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
    '''Роутер для логаута юзеров'''

    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile_user(request) -> HttpResponse:
    '''Роутер для отображения профиля юзера'''

    links_list = request.user.links.order_by('-created_at')
    return render(request, 'users/profile.html', {
        'user': request.user,
        'links': links_list
    })
