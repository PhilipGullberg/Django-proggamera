# Generated by Django 3.2.7 on 2022-03-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_fillinblanks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillinblanks',
            name='code',
            field=models.TextField(max_length=1000),
        ),
    ]
