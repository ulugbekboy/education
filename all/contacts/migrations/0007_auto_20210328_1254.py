# Generated by Django 3.1.7 on 2021-03-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='study',
            field=models.CharField(blank=True, choices=[('Бакалавр', 1), ('Foundation', 2), ('Магистратура', 3)], max_length=1000, verbose_name='Study status'),
        ),
    ]
