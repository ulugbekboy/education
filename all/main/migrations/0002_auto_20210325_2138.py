# Generated by Django 3.1.7 on 2021-03-25 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantage',
            options={'verbose_name': 'Преимущества', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Вопросы & Ответы', 'verbose_name_plural': 'Вопросы & Ответы'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name': 'Отзывы', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
