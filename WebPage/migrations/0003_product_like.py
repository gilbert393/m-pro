# Generated by Django 3.2.7 on 2021-09-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Like',
            field=models.BooleanField(null=True),
        ),
    ]
