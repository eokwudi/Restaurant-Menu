# Generated by Django 3.0.3 on 2020-02-25 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parm',
            name='size',
        ),
        migrations.RemoveField(
            model_name='pasta',
            name='size',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='size',
        ),
    ]
