# Generated by Django 5.1.4 on 2024-12-21 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_userprofile_bio_en_userprofile_bio_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saveitem',
            old_name='save',
            new_name='saved',
        ),
    ]
