# Generated by Django 3.2.7 on 2022-05-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0023_auto_20220520_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentexcercises',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profilepage.student'),
        ),
    ]
