# Generated by Django 3.2.7 on 2022-05-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_auto_20220520_1001'),
        ('profilepage', '0021_auto_20220520_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excercise',
            name='fill_excercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.fillinblanks'),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='quiz_excercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.quiz'),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='read_excercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='excercise_subchapter', to='profilepage.subchapters'),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='video_excercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.videos'),
        ),
        migrations.AlterField(
            model_name='subchapters',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.videos'),
        ),
    ]
