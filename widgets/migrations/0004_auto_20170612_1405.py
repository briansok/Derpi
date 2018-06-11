# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0003_widgets_widget_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgets',
            name='sensors',
            field=models.ForeignKey(blank=True, to='sensors.Sensors', null=True),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='widget_type',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[('CL', 'Clock'), ('WE', 'Weather')]),
        ),
    ]
