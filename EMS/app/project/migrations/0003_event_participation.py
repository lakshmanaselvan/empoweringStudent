# Generated by Django 5.0 on 2024-03-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_categories_categorie_rename_events_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participation',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default='Both', max_length=20),
        ),
    ]
