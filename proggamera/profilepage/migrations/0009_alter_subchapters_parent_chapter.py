# Generated by Django 3.2.7 on 2022-02-09 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0008_auto_20220209_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subchapters',
            name='parent_chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='profilepage.chapters'),
        ),
    ]
