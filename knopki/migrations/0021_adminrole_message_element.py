# Generated by Django 4.2.3 on 2023-08-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0020_adminrole_frame_adminrole_waitmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminrole',
            name='message_element',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='knopki.message_element'),
        ),
    ]
