# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='hotel_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='rental_price',
            field=models.FloatField(),
        ),
    ]
