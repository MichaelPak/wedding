# coding=utf-8
from django.contrib import admin

# Register your models here.
from web.models import Registration, Hotel


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'comment', 'registered_dt_formatted', 'is_submit']
    list_editable = ['is_submit']

    def registered_dt_formatted(self, obj):
        return obj.registered_dt.strftime("%d.%m.%Y %H:%M")

    registered_dt_formatted.admin_order_field = 'registered_dt'
    registered_dt_formatted.short_description = u'Дата регистрации'


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'comment', 'is_submit']
    list_editable = ['is_submit']

