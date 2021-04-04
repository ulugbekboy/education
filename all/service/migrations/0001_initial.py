# Generated by Django 3.1.7 on 2021-03-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='service_list/images', verbose_name='Service_list_image')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Service_List',
                'verbose_name_plural': 'Service_Lists',
            },
        ),
    ]