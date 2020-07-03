# Generated by Django 3.0.4 on 2020-03-30 07:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('date', models.DateField(auto_now_add=True)),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Сортировать')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['order'],
            },
        ),
    ]
