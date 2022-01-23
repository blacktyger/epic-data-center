# Generated by Django 4.0 on 2022-01-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coingecko_feed', '0002_coingecko_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='coingecko',
            name='btc_vs_usd',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=32),
            preserve_default=False,
        ),
    ]
