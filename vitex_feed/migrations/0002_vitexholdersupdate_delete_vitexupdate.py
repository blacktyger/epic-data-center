# Generated by Django 4.0 on 2021-12-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitex_feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VitexHoldersUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('holders_count', models.IntegerField()),
                ('holders_stats', models.JSONField(default=dict)),
            ],
        ),
        migrations.DeleteModel(
            name='VitexUpdate',
        ),
    ]
