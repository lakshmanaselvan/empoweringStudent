# Generated by Django 5.0 on 2024-03-22 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.venue'),
        ),
    ]
