# Generated by Django 4.2.7 on 2024-01-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='usd',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]