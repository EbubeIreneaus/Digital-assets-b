# Generated by Django 4.2.7 on 2024-01-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='channel',
            field=models.CharField(blank=True, default='BTC', max_length=40, null=True),
        ),
    ]
