# Generated by Django 4.1.7 on 2023-02-15 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citybike', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stationextra',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]