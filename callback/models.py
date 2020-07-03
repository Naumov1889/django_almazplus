from django.db import models

class Callback(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.CharField(max_length=55, blank=True, verbose_name="Почта")
    vacancy = models.CharField(max_length=50, blank=True, verbose_name="Вакансия")
    product = models.CharField(max_length=50, blank=True, verbose_name="Продукт")

    def __str__(self):
        return self.name + " / " + self.phone + " / " + self.email + " / " + self.vacancy + " / " + self.product

    class Meta(object):
        verbose_name = "Запрос на обратную связь"
        verbose_name_plural = "Запросы на обратную связь"