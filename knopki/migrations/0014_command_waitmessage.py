# Generated by Django 4.2.3 on 2023-08-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0013_remove_command_helptext_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='waitmessage',
            field=models.BooleanField(default=False),
        ),
    ]