# Generated by Django 5.1.4 on 2024-12-21 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_alter_userprofile_options_alter_userprofile_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
    ]