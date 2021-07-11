from django.contrib import admin
from .models import Url

# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display = ('address','status')
admin.site.register(Url, UrlAdmin)