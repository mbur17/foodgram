# Generated by Django 4.2.17 on 2025-01-25 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlmap',
            options={'verbose_name': 'Короткую ссылку', 'verbose_name_plural': 'Короткие ссылки'},
        ),
    ]
