# Generated by Django 4.0 on 2021-12-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer_feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='diff',
        ),
        migrations.AddField(
            model_name='block',
            name='network_hashrate',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='block',
            name='target_diffs',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='block',
            name='total_diffs',
            field=models.JSONField(default={}),
        ),
    ]
