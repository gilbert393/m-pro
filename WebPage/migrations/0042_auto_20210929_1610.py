# Generated by Django 3.2.7 on 2021-09-29 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0041_auto_20210927_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Sub_Topic',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 10, 32, 214515)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 10, 32, 214515)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 10, 32, 214515)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 10, 32, 214515)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 10, 32, 214515)),
        ),
    ]