# Generated by Django 3.2.7 on 2021-09-29 14:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0047_auto_20210929_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 26, 5, 617248)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 26, 5, 617248)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 26, 5, 617248)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 26, 5, 617248)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 29, 16, 26, 5, 617248)),
        ),
        migrations.CreateModel(
            name='multipleQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option_1', models.CharField(max_length=1000)),
                ('Option_2', models.CharField(max_length=1000)),
                ('Option_3', models.CharField(max_length=1000)),
                ('Option_4', models.CharField(max_length=1000)),
                ('Answer', models.CharField(max_length=1000)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPage.question')),
            ],
        ),
    ]
