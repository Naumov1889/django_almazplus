from django import forms


class CallbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
        'class': 'input input-container__input',
        'id': ''
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Номер телефона',
        'class': 'input input-container__input',
        'id': ''
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'E-mail',
        'class': 'input input-container__input',
        'id': ''
    }))
    vacancy = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Вакансия',
        'class': 'input input-container__input',
        'id': ''
    }))
    product = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Продукт',
        'class': 'input input-container__input',
        'id': ''
    }))

