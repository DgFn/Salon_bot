# Generated by Django 4.2 on 2023-08-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knopki', '0008_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='имя элемента')),
                ('handler', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='обработчик')),
            ],
        ),
        migrations.CreateModel(
            name='Text_element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default=None, null=True, verbose_name='текст')),
                ('message_element', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='knopki.message_element')),
            ],
        ),
        migrations.CreateModel(
            name='Button_element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default=None, null=True, verbose_name='текст')),
                ('callback_data', models.TextField(blank=True, default=None, null=True, verbose_name='параметр в кнопке')),
                ('message_element', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='knopki.message_element')),
            ],
        ),
    ]
