# Generated by Django 2.2.6 on 2019-10-10 20:35

import adminsortable.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('default_format', models.CharField(choices=[('form', 'Form'), ('json', 'JSON')], default='json', max_length=60, verbose_name='Default format')),
            ],
            options={
                'verbose_name': 'Input settings',
                'verbose_name_plural': 'Input settings',
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_source', models.BooleanField(blank=True, default=True, verbose_name='Internal source')),
                ('format', models.CharField(choices=[('form', 'Form'), ('json', 'JSON')], default='json', max_length=60, verbose_name='Default format')),
                ('processed', models.BooleanField(blank=True, default=False, verbose_name='Processed')),
                ('raw_content', models.TextField(verbose_name='Raw content')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inputs', to='inputflow.InputSettings', verbose_name='Settings')),
            ],
            options={
                'verbose_name': 'Input',
                'verbose_name_plural': 'Inputs',
            },
        ),
        migrations.CreateModel(
            name='InputSettingsField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_position', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('input_name', models.CharField(max_length=60, verbose_name='Input name')),
                ('output_name', models.CharField(blank=True, default='', max_length=60, verbose_name='Field name')),
                ('example_value', models.TextField(blank=True, default='', verbose_name='Example value')),
                ('date_format', models.CharField(blank=True, default='', max_length=40, verbose_name='Date format')),
                ('default_value', models.TextField(blank=True, default='', verbose_name='Default value')),
                ('exclude_if_empty', models.BooleanField(blank=True, default=False, verbose_name='Exclude if empty')),
                ('omit', models.BooleanField(blank=True, default=False, verbose_name='Omit')),
                ('settings', adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_fields', to='inputflow.InputSettings', verbose_name='Input settings')),
            ],
            options={
                'verbose_name': 'Input field',
                'verbose_name_plural': 'Input fields',
                'ordering': ['field_position'],
                'unique_together': {('settings', 'input_name')},
            },
        ),
    ]
