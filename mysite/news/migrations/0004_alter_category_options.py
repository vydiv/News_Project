# Generated by Django 3.2.7 on 2021-12-01 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211201_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]