# Generated by Django 2.0b1 on 2017-11-05 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Creation date')),
                ('is_public', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Last update')),
                ('name', models.CharField(max_length=255)),
                ('template', models.CharField(choices=[('default', 'Default Template')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shared_with', models.ManyToManyField(related_name='co_owners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CollectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_description', models.CharField(max_length=100)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Creation date')),
                ('is_public', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Last update')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='EntityResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', 'Entity Image'), ('url', 'Entity Link')], max_length=25)),
                ('data', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collectionitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Entity'),
        ),
        migrations.AddField(
            model_name='collectionitem',
            name='notes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Note'),
        ),
    ]
