# Generated by Django 5.1 on 2024-09-07 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sortinghat', '0002_rename_house_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='user',
        ),
    ]
