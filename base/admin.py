from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from .models import Vacancy, Contact, Product, IndexPageSlide, IndexPageFeature, AboutPageText, AboutPageImg, \
    ConfidentialityAndTerms


@admin.register(Vacancy)
class VacancyAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'phone', 'email', 'location')
    list_editable = ('title', 'subtitle', 'phone', 'email', 'location')
    list_display_links = ('order',)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag',)
    list_display_links = ('image_tag', 'title')
    readonly_fields = ['image_tag']


@admin.register(IndexPageSlide)
class IndexPageSlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'picture', 'title', 'subtitle', 'link')
    list_editable = ('picture', 'title', 'subtitle', 'link')
    list_display_links = ('order', 'image_tag')


@admin.register(IndexPageFeature)
class IndexPageFeatureAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'picture', 'text',)
    list_editable = ('picture', 'text',)
    list_display_links = ('order', 'image_tag')


class AboutPageImgInline(SortableInlineAdminMixin, admin.TabularInline):  # or admin.StackedInline
    model = AboutPageImg


@admin.register(AboutPageText)
class AboutPageImgAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (AboutPageImgInline,)


admin.site.register(ConfidentialityAndTerms)
