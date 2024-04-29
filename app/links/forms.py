from django import forms


class TinyUrlForm(forms.Form):
    '''Форма для главной страницы'''

    target_url = forms.URLField(
        required=True, 
        label='Shorter URLs', 
        help_text='Введите URL, который хотите сократить'
    )
