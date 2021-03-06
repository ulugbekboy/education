# Generated by Django 3.1.7 on 2021-03-26 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_auto_20210325_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Faculty')),
                ('study_year', models.CharField(blank=True, max_length=100, verbose_name='Study_year')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.RemoveField(
            model_name='bachelor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bachelor',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='bachelor',
            name='study_year',
        ),
        migrations.RemoveField(
            model_name='masters',
            name='name',
        ),
        migrations.RemoveField(
            model_name='masters',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='masters',
            name='study_year',
        ),
        migrations.AddField(
            model_name='bachelor',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
        migrations.AddField(
            model_name='masters',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.faculty'),
        ),
    ]
