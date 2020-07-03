from django.shortcuts import render, get_object_or_404
from .models import Vacancy, Contact, Product, IndexPageSlide, IndexPageFeature, AboutPageText, AboutPageImg, ConfidentialityAndTerms


def home_page(request):
    products = Product.objects.all()

    slides = IndexPageSlide.objects.all()
    features = IndexPageFeature.objects.all()
    context = {
        'products': products,
        'slides': slides,
        'features': features
    }

    return render(request, 'base/index.html', context)


def contact_page(request):
    # contact_set = Contact.objects.all().order_by('order')
    # contact_set_processed = []
    #
    # for contact in contact_set.iterator():
    #     phone_list = contact.phone.split(";")
    #     phone_list = [phone.strip() for phone in phone_list]
    #
    #     email_list = contact.email.split(";")
    #     email_list = [email.strip() for email in email_list]
    #
    #     contact = contact.__dict__
    #     contact.update({"phone": phone_list})
    #     contact.update({"email": email_list})
    #
    #     contact_set_processed.append(contact)
    #
    # context = {
    #     'contact_set': contact_set_processed
    # }
    return render(request, 'base/contact.html')


def confidentiality_page(request):
    return render(request, 'base/confidentiality.html', {'text': ConfidentialityAndTerms.objects.all().first()})


def terms_page(request):
    return render(request, 'base/terms.html', {'text': ConfidentialityAndTerms.objects.all().first()})


def vacancy(request):
    context = {
        'vacancies': Vacancy.objects.all()
    }

    return render(request, 'base/vacancy.html', context)


def product_page(request, slug):
    # product = get_object_or_404(Product, slug=slug),
    # print(product.title)
    # print(product)
    context = {
        'product': get_object_or_404(Product, slug=slug)
    }

    return render(request, 'base/product.html', context)


def about_page(request):
    about_page_text = AboutPageText.objects.all().first()
    about_page_imgs = AboutPageImg.objects.all()
    context = {
        'about_page_text': about_page_text,
        'about_page_imgs': about_page_imgs
    }
    return render(request, 'base/about.html', context)
