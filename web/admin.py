from django.contrib import admin

# Register your models here.
from web.models import Registration, Hotel


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'comment', 'is_submit']
    list_editable = ['is_submit']


class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'comment', 'is_submit']
    list_editable = ['is_submit']


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Hotel, HotelAdmin)
