# Generated by Django 4.0.3 on 2023-05-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_menu_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='serial_number',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Serial number'),
        ),
    ]