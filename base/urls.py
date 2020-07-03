from django.urls import path
from .views import home_page, contact_page, confidentiality_page, terms_page, vacancy, product_page, about_page

app_name = "base"
urlpatterns = [
    path('', home_page, name="home_page"),
    path('contact/', contact_page, name="contact_page"),
    path('about/', about_page, name="about_page"),
    path('product/<slug>/', product_page, name="product_page"),
    path('vacancies/', vacancy, name="vacancy"),
    path('confidentiality/', confidentiality_page, name="confidentiality_page"),
    path('terms/', terms_page, name="terms_page"),
]
