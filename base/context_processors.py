from callback.forms import CallbackForm
from .models import Contact


def callback(request):
    return {
        "callback_form": CallbackForm
    }


def contact(request):
    contact_set = Contact.objects.all().order_by('order')
    contact_set_processed = []

    for contact in contact_set.iterator():
        phone_list = contact.phone.split(";")
        phone_list = [phone.strip() for phone in phone_list]

        email_list = contact.email.split(";")
        email_list = [email.strip() for email in email_list]

        contact = contact.__dict__
        contact.update({"phone": phone_list})
        contact.update({"email": email_list})

        contact_set_processed.append(contact)

    return {
        "contact_set": contact_set_processed
    }
