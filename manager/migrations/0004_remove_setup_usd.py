# Generated by Django 4.2.7 on 2024-01-01 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_setup_usd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setup',
            name='usd',
        ),
    ]