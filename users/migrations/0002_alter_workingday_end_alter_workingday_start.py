# Generated by Django 5.1.4 on 2025-01-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingday',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='start',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
