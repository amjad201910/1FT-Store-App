# Generated by Django 4.1 on 2022-09-05 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_dessert_price_dessert_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='Image',
        ),
    ]