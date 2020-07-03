from django.contrib import admin
from .models import Callback

class CallbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'vacancy', 'product')
    readonly_fields = ['name', 'phone', 'email', 'vacancy', 'product']

admin.site.register(Callback, CallbackAdmin)
