# Generated by Django 5.0 on 2024-03-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_registration_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
