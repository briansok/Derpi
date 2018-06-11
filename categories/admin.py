from django.contrib import admin
from .models import Categories

class EntryCategories(admin.ModelAdmin):
    list_display = ('title', 'created')

admin.site.register(Categories, EntryCategories)

