# Generated by Django 3.2.7 on 2021-09-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0006_auto_20210925_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=1000),
        ),
    ]
