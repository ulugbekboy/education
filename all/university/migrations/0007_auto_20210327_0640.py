# Generated by Django 3.1.7 on 2021-03-27 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_auto_20210327_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study_form',
            name='faculty',
        ),
        migrations.AddField(
            model_name='study_form',
            name='faculty',
            field=models.ManyToManyField(blank=True, null=True, to='university.Faculty'),
        ),
        migrations.RemoveField(
            model_name='university',
            name='faculty',
        ),
        migrations.AddField(
            model_name='university',
            name='faculty',
            field=models.ManyToManyField(blank=True, null=True, related_name='faculty_name', to='university.Faculty', verbose_name='Faculty'),
        ),
        migrations.RemoveField(
            model_name='university',
            name='study_form',
        ),
        migrations.AddField(
            model_name='university',
            name='study_form',
            field=models.ManyToManyField(null=True, to='university.Study_form', verbose_name='Форма обучения'),
        ),
    ]