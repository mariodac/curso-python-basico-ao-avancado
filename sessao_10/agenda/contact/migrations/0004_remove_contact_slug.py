# Generated by Django 5.1.5 on 2025-02-03 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='slug',
        ),
    ]
