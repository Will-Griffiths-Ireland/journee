# Generated by Django 4.2.2 on 2023-06-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='public',
            new_name='is_public',
        ),
    ]
