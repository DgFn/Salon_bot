# Generated by Django 4.2.3 on 2023-08-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0019_adminrole_alter_user_usernick'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminrole',
            name='frame',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adminrole',
            name='waitmessage',
            field=models.BooleanField(default=False),
        ),
    ]
