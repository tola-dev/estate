# Generated by Django 3.1 on 2022-10-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='ppty',
        ),
        migrations.RemoveField(
            model_name='location',
            name='til',
        ),
    ]
