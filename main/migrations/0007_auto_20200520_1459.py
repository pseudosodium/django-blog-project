# Generated by Django 3.0.6 on 2020-05-20 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200520_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 14, 59, 54, 53507), verbose_name='Date Published'),
        ),
    ]