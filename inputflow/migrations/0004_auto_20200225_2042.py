# Generated by Django 2.2.7 on 2020-02-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputflow', '0003_auto_20191011_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='raw_content_type',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Raw content type'),
        ),
        migrations.AlterField(
            model_name='input',
            name='format',
            field=models.CharField(choices=[('form', 'Form'), ('multipart', 'Multipart form'), ('json', 'JSON')], default='json', max_length=60, verbose_name='Default format'),
        ),
        migrations.AlterField(
            model_name='inputsettings',
            name='default_format',
            field=models.CharField(choices=[('form', 'Form'), ('multipart', 'Multipart form'), ('json', 'JSON')], default='json', max_length=60, verbose_name='Default format'),
        ),
    ]