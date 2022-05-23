# Generated by Django 3.2.7 on 2022-05-20 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0022_auto_20220520_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subchapters',
            name='video',
        ),
        migrations.CreateModel(
            name='StudentExcercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excercises', models.ManyToManyField(to='profilepage.Excercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profilepage.student')),
            ],
        ),
    ]
