# Generated by Django 4.0.2 on 2022-10-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_resultresponse_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultresponse',
            name='result',
            field=models.TextField(),
        ),
    ]
