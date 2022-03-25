# Generated by Django 3.2.7 on 2022-03-23 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0016_alter_student_license_active'),
        ('courses', '0021_visitedpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitedpage',
            name='subchapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profilepage.subchapters'),
            preserve_default=False,
        ),
    ]
