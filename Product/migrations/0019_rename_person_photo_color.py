# Generated by Django 4.1 on 2022-09-05 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_rename_color_photo_person_delete_p'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='person',
            new_name='color',
        ),
    ]
