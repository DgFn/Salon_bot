# Generated by Django 4.2.3 on 2023-08-16 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0012_user_jopa_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='helptext',
        ),
        migrations.RemoveField(
            model_name='command',
            name='messagefromuser',
        ),
        migrations.RemoveField(
            model_name='command',
            name='name_functions',
        ),
    ]