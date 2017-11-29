# Generated by Django 2.0b1 on 2017-11-17 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_entityresource_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='co_owners', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='entityresource',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('url', 'Link')], default='url', max_length=25),
        ),
    ]
