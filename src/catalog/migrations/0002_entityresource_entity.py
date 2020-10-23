# Generated by Django 2.0b1 on 2017-11-07 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="entityresource",
            name="entity",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.Entity",
            ),
        ),
    ]
