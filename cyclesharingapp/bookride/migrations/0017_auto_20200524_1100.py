# Generated by Django 3.0.5 on 2020-05-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookride', '0016_auto_20200524_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='drop_location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='fare',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='from_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='pickup_location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='to_time',
            field=models.TimeField(),
        ),
    ]
