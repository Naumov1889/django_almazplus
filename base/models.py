from django.utils import timezone
from django.db import models
from pytils import translit
# from base.utils import get_image_path
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import os
from pytils import translit


class Vacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    text = RichTextField(verbose_name="Текст")
    date = models.DateField(default=timezone.now, verbose_name="Дата")

    def __str__(self):
        return self.title + " / " + str(self.date)

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", null=True, blank=True)
    subtitle = models.CharField(max_length=100, verbose_name="Подзаголовок", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="Почта", null=True, blank=True)
    location = models.CharField(max_length=100, verbose_name="Адрес", null=True, blank=True)
    coordinates_center = models.CharField(max_length=50, verbose_name="Коорд-ты центра", null=True, blank=True)
    coordinates_center_mobile = models.CharField(max_length=50, verbose_name="Коорд-ты центра в моб. версии", null=True, blank=True)
    coordinates_placemark = models.CharField(max_length=50, verbose_name="Коорд-ты метки", null=True, blank=True)

    def __str__(self):
        contact_promo = self.title if self.title else str(self.order)
        return contact_promo

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    def get_image_path(self, filename):
        name, extension = os.path.splitext(filename)
        path = ''.join([translit.slugify(name)])
        return path + extension

    title = models.CharField(max_length=100, verbose_name="Название")
    slug = AutoSlugField(populate_from="title", always_update="True", unique="True", db_index=True, max_length=220)
    picture_card = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото карточки")
    picture_article = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото заголовка статьи")
    subtitle = models.TextField(verbose_name="Подзаголовок статьи", null=True, blank=True)
    text = RichTextUploadingField(verbose_name="Текст статьи")

    def __str__(self):
        return self.title

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture_card))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True


class IndexPageSlide(models.Model):
    def get_image_path(self, filename):
        name, extension = os.path.splitext(filename)
        path = ''.join([translit.slugify(name)])
        return path + extension

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=300, verbose_name="Подзаголовок")
    picture = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото")
    link = models.CharField(max_length=300, verbose_name="Ссылка", default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Слайдер на главной странице"
        verbose_name_plural = "Слайдер на главной странице"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True


class IndexPageFeature(models.Model):
    def get_image_path(self, filename):
        name, extension = os.path.splitext(filename)
        path = ''.join([translit.slugify(name)])
        return path + extension

    text = models.CharField(max_length=100, verbose_name="Текст")
    picture = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото")

    def __str__(self):
        return self.text

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Преимущество на главной странице"
        verbose_name_plural = "Преимущества на главной странице"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True


# class AboutPageText(models.Model):
#     text = RichTextUploadingField(verbose_name="Текст")
#
#     def __str__(self):
#         return "О компании"
#
#     order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")
#
#     class Meta(object):
#         ordering = ['order']
#         verbose_name = "О компании"
#         verbose_name_plural = "О компании"
#
#
# class AboutPageImg(models.Model):
#     def get_image_path(self, filename):
#         name, extension = os.path.splitext(filename)
#         path = ''.join([translit.slugify(name)])
#         return path + extension
#
#     picture = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото")
#     about_page_text = models.ForeignKey(AboutPageText, blank=True, null=True, on_delete=models.CASCADE)
#
#     order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")
#
#     class Meta(object):
#         ordering = ['order']
#         verbose_name = "Логотип компании"
#         verbose_name_plural = "Логотипы компании"
#
#     def image_tag(self):
#         from django.utils.html import mark_safe
#         return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture))
#
#     image_tag.short_description = 'Фото'
#     image_tag.allow_tags = True
#
#     def __str__(self):
#         return self.order


class AboutPageText(models.Model):
    text = RichTextUploadingField(verbose_name="Текст")

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self):
        return "О компании"


class AboutPageImg(models.Model):
    def get_image_path(self, filename):
        name, extension = os.path.splitext(filename)
        path = ''.join([translit.slugify(name)])
        return path + extension

    picture = models.ImageField(upload_to=get_image_path, default=None, verbose_name="Фото")
    about_page_text = models.ForeignKey(AboutPageText, blank=True, null=True, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Лого"
        verbose_name_plural = "Лого"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture))

    image_tag.short_description = 'Фото'
    image_tag.allow_tags = True


class ConfidentialityAndTerms(models.Model):
    confidentiality = RichTextUploadingField(verbose_name="Политика конфиденциальности")
    terms = RichTextUploadingField(verbose_name="Пользовательское соглашение")


    class Meta(object):
        verbose_name = "Конфиденциальность и соглашение"
        verbose_name_plural = "Конфиденциальность и соглашение"

    def __str__(self):
        return "Конфиденциальность и соглашение"