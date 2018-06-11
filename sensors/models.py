from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Sensors(models.Model):
    switch = 'SW'
    output = 'OU'
    slider = 'SL'
    sensor_types_choices = (
        (switch, 'On off switch'),
        (output, 'Sensor output'),
        (slider, 'Data slider'),
        )
    sensor_types = models.CharField(
        max_length=2,
        choices=sensor_types_choices,
        default=switch,
        )
    category = models.ForeignKey('categories.Categories', related_name='category', on_delete=models.CASCADE, null=True)
    controller = models.ForeignKey('controllers.Controllers', related_name='controller', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    value = models.IntegerField(null=True)
    gpio = models.IntegerField(null=True)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'
        ordering = ['-created']

