# Generated by Django 3.1 on 2022-11-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppty', '0006_auto_20221105_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_property',
            name='property_price',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='mortgage_property',
            name='property_price',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='rent_property',
            name='property_price',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='sale_property',
            name='property_price',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]