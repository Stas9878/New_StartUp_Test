from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', help_text='Придумайте логин')
    password1 = forms.CharField(label='Пароль', help_text='Придумайте пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
        
        help_texts = {
            'email': 'Введите вашу электронную почту'
        }