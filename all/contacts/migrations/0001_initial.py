# Generated by Django 3.1.7 on 2021-03-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, verbose_name='Name')),
                ('surname', models.CharField(blank=True, max_length=1000, verbose_name='Surname')),
                ('birth_date', models.DateTimeField(blank=True, verbose_name='Birth date')),
                ('city', models.CharField(blank=True, max_length=1000, verbose_name='City')),
                ('phone', models.CharField(blank=True, max_length=1000, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('english', models.CharField(blank=True, choices=[('Начинающий (А1-А2)', 1), ('Средний (В1-В2),2', 'Продвинутый(С1-С2)')], max_length=1000, verbose_name='English level')),
                ('study', models.CharField(blank=True, choices=[('Бакалавр', 1), ('Foundation', 2), ('Магистр', 1)], max_length=1000, verbose_name='Study status')),
                ('description', models.TextField(verbose_name='Info')),
                ('take_date', models.DateTimeField(blank=True, verbose_name='Taking date')),
            ],
            options={
                'verbose_name': 'Consulting',
                'verbose_name_plural': 'Consulting',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=1000, verbose_name='Phone')),
                ('telegram', models.CharField(blank=True, max_length=1000, verbose_name='Telegram')),
                ('facebook', models.CharField(blank=True, max_length=1000, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=1000, verbose_name='Instagram')),
                ('working_time', models.CharField(blank=True, max_length=1000, verbose_name='Working_Time')),
                ('address', models.CharField(blank=True, max_length=1000, verbose_name='Address')),
                ('address1', models.CharField(blank=True, max_length=1000, verbose_name='Address')),
                ('address2', models.CharField(blank=True, max_length=1000, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Contact_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('phone', models.CharField(blank=True, default='+998', max_length=100, verbose_name='Phone')),
                ('content', models.CharField(blank=True, max_length=100, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Contact_Forms',
            },
        ),
    ]
