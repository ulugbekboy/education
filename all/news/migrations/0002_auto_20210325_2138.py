# Generated by Django 3.1.7 on 2021-03-25 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
    ]