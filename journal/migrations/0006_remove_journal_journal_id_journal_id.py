# Generated by Django 4.2.2 on 2023-06-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_remove_journal_id_alter_journal_journal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='journal_id',
        ),
        migrations.AddField(
            model_name='journal',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
