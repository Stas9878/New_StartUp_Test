from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    '''Форма аутентификации'''

    username = forms.CharField(label='Логин', help_text='Введите ваш логин')
    password = forms.CharField(label='Пароль', help_text='Введите ваш пароль')


class RegisterUserForm(forms.ModelForm):
    '''Форма регистрации'''

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


    def clean_password2(self) -> str:
        '''Метод сравнения password1 и password2'''
        
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password1']
    

    def clean_email(self) -> str:
        '''Метод для проверки - не занят ли email другим юзером'''
        
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email занят')
        return email
    
