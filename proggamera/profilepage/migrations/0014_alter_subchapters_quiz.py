# Generated by Django 3.2.7 on 2022-02-14 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_quiz_quiz_name'),
        ('profilepage', '0013_subchapters_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subchapters',
            name='quiz',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.quiz'),
        ),
    ]
