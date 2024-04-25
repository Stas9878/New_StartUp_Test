from django import forms


class TinyUrlForm(forms.Form):
    target_url = forms.URLField(required=True, label='Введите URL, который хотите сократить')
