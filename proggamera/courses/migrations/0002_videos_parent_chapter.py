# Generated by Django 3.2.7 on 2022-02-14 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0010_auto_20220211_1311'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='parent_chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profilepage.subchapters'),
            preserve_default=False,
        ),
    ]
