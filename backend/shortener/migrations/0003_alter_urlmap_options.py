# Generated by Django 4.2.17 on 2025-02-09 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_urlmap_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlmap',
            options={'ordering': ('recipe__created_at',), 'verbose_name': 'Короткую ссылку', 'verbose_name_plural': 'Короткие ссылки'},
        ),
    ]
