# Generated by Django 5.0 on 2024-03-22 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_registration_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='is_staff',
        ),
    ]
