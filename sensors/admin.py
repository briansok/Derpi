from django.contrib import admin
from .models import Sensors

class EntrySensors(admin.ModelAdmin):
    list_display = ('title', 'created')

admin.site.register(Sensors, EntrySensors)
