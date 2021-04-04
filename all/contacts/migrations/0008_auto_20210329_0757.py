# Generated by Django 3.1.7 on 2021-03-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20210328_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='english',
            field=models.CharField(blank=True, choices=[('Начинающий (А1-А2)', 'Начинающий (А1-А2)'), ('Средний (В1-В2)', 'Средний (В1-В2)'), ('Продвинутый(С1-С2)', 'Продвинутый(С1-С2)')], max_length=1000, verbose_name='English level'),
        ),
        migrations.AlterField(
            model_name='consulting',
            name='study',
            field=models.CharField(blank=True, choices=[('Бакалавр', 'Бакалавр'), ('Foundation', 'Foundation'), ('Магистратура', 'Магистратура')], max_length=1000, verbose_name='Study status'),
        ),
    ]