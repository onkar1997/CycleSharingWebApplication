# Generated by Django 3.0.5 on 2020-05-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookride', '0010_auto_20200523_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='drop_location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='pickup_location',
            field=models.CharField(default='', max_length=50),
        ),
    ]
