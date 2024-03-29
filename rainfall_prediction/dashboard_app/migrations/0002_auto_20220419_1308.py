# Generated by Django 3.2.9 on 2022-04-19 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='cloud',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='dewpoint',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='humidity',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='max_temp',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_temp',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='pressure',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='sunshine',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='temp',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='wind_direction',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='wind_speed',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
    ]
