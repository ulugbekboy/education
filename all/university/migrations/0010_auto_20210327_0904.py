# Generated by Django 3.1.7 on 2021-03-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_auto_20210327_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='number',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Rating'),
        ),
    ]
