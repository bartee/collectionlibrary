# Generated by Django 2.0 on 2017-12-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20171208_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityresource',
            name='data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entityresource',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
