# Generated by Django 4.2 on 2023-08-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0010_command_message_element'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='action',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='helptext',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='masframe',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='messagefromuser',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='name_functions',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
