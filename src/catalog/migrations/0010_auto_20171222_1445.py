# Generated by Django 2.0 on 2017-12-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20171214_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='rating',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
