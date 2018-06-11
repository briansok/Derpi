from django.contrib import admin
from .models import Controllers

class EntryControllers(admin.ModelAdmin):
    list_display = ('title', 'created')

admin.site.register(Controllers, EntryControllers)

