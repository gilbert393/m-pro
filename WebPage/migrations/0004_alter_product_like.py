# Generated by Django 3.2.7 on 2021-09-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0003_product_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Like',
            field=models.BooleanField(),
        ),
    ]
