from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Widgets(models.Model):
    sensors = models.ForeignKey('sensors.Sensors', on_delete=models.CASCADE, null=True, blank=True)
    controllers = models.ForeignKey('controllers.Controllers', on_delete=models.CASCADE, null=True, blank=True)
    widget_types = (
        ('CL', 'Clock'),
        ('WE', 'Weather'),
        )
    widget_type = models.CharField(
        max_length=2,
        choices=widget_types,
        null=True,
        blank=True,
        )
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'
        ordering = ['-created']
