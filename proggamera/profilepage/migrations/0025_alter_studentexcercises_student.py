# Generated by Django 3.2.7 on 2022-05-23 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0024_alter_studentexcercises_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentexcercises',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profilepage.student'),
            preserve_default=False,
        ),
    ]
