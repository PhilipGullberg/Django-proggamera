# Generated by Django 3.2.7 on 2022-03-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_videowatched'),
    ]

    operations = [
        migrations.AddField(
            model_name='videowatched',
            name='watchtime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
