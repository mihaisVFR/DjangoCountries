# Generated by Django 4.2.1 on 2023-05-23 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='languages',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
