# Generated by Django 3.1.7 on 2021-03-28 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0012_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='country', to='university.country'),
        ),
    ]
