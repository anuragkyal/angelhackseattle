# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friend_user_id', models.CharField(max_length=200)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=200)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_price', models.IntegerField()),
                ('rental_name', models.CharField(max_length=200)),
                ('rental_price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='interest',
            name='plan_id',
            field=models.ForeignKey(to='plans.Plan'),
            preserve_default=True,
        ),
    ]
