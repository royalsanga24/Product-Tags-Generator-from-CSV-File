# Generated by Django 4.0.2 on 2022-10-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultresponse',
            name='result',
            field=models.JSONField(),
        ),
    ]
