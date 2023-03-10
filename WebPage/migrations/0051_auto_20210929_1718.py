# Generated by Django 3.2.7 on 2021-09-29 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0050_auto_20210929_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Q_user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 17, 18, 0, 400439)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 17, 18, 0, 400439)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 17, 18, 0, 400439)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 17, 18, 0, 400439)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 17, 18, 0, 400439)),
        ),
    ]
