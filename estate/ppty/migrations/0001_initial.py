# Generated by Django 3.1 on 2022-10-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('til', models.TextField()),
                ('loct', models.TextField()),
                ('ppty', models.TextField()),
                ('features', models.BooleanField(default=False)),
            ],
        ),
    ]
