# Generated by Django 3.0.4 on 2020-04-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0003_auto_20200331_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='callback',
            name='product',
            field=models.CharField(blank=True, max_length=50, verbose_name='Продукт'),
        ),
    ]
