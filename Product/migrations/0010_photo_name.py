# Generated by Django 4.1 on 2022-09-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_photo_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='Name',
            field=models.CharField(default='sa', max_length=42),
        ),
    ]