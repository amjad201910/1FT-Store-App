# Generated by Django 4.1 on 2022-09-04 21:46

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=Product.models.upload_path),
        ),
    ]
