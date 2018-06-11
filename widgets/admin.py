from django.contrib import admin
from .models import Widgets

class EntryControllers(admin.ModelAdmin):
    list_display = ('created', 'created')

admin.site.register(Widgets, EntryControllers)

