# Generated by Django 4.2.7 on 2024-02-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='enable_verification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='verification_plus',
            field=models.BooleanField(default=False),
        ),
    ]
