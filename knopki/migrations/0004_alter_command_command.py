# Generated by Django 4.2 on 2023-07-31 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0003_command_masframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.CharField(default='', max_length=100),
        ),
    ]
