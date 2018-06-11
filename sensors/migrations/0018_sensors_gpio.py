# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0017_auto_20170228_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='gpio',
            field=models.IntegerField(null=True),
        ),
    ]
