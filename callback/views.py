from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Callback
from .forms import CallbackForm


def record_callback(request):
    form = CallbackForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        vacancy = form.cleaned_data.get('vacancy')
        product = form.cleaned_data.get('product')

        callback = Callback(
            name=name,
            phone=phone,
            email=email,
            vacancy=vacancy,
            product=product,
        )

        superusers_emails = User.objects.filter(is_superuser=True).values_list('email', flat=True)

        title = "Запрос на обратный звонок"
        message = f'Имя: {name}\nТелефон: {phone}'

        if vacancy != "—":
            title = "Запрос на вакансию"
            message = message + "\nВакансия: " + vacancy


        if product != "—":
            title = "Запрос на оформление товара"
            message = message + "\nПочта: " + email + "\nПродукт: " + product

        send_mail(
            title,
            message,
            '"almazplus.ru" <settings.EMAIL_HOST_USER>',
            list(superusers_emails)
        )

        callback.save()

        return HttpResponse('success')
    return HttpResponse('invalid')
