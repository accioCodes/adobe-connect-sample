# Generated by Django 3.0.8 on 2020-07-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backprojectapi', '0006_auto_20200730_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='startTime',
            field=models.TextField(max_length=50),
        ),
    ]
