# Generated by Django 4.1 on 2022-09-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0020_rename_color_photo_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='Cover',
            field=models.BooleanField(default=False),
        ),
    ]
