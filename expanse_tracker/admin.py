from django.contrib import admin
from .models import *

# Admin View Custom


class expanseAdmin(admin.ModelAdmin):
    list_display = ['Type', 'Amount', 'Date']


# Register your models here.
admin.site.register(Expanse, expanseAdmin)
admin.site.register(Type)
