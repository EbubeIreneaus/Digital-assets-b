# Generated by Django 4.2.7 on 2023-11-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]