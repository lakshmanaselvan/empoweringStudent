# Generated by Django 5.0 on 2024-03-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_registration_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
