# Generated by Django 4.2.3 on 2023-08-30 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0022_remove_adminrole_frame_remove_adminrole_waitmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminrole',
            name='button_element',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='knopki.button_element'),
        ),
    ]