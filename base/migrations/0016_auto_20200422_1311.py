# Generated by Django 3.0.4 on 2020-04-22 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_indexpageslide_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Подзаголовок статьи'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
