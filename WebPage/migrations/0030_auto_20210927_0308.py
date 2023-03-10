# Generated by Django 3.2.7 on 2021-09-27 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0029_auto_20210926_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 3, 8, 12, 249536)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 3, 8, 12, 250543)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 3, 8, 12, 248536)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 3, 8, 12, 250543)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 3, 8, 12, 245526)),
        ),
    ]
