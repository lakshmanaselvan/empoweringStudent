# Generated by Django 5.0 on 2024-03-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_registration_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='has_module_perms',
            field=models.BooleanField(default=False),
        ),
    ]
