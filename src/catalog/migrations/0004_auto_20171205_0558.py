# Generated by Django 2.0 on 2017-12-05 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20171117_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitem',
            name='item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Entity'),
        ),
    ]
