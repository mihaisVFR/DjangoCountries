# Generated by Django 4.2.1 on 2023-05-25 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_delete_test'),
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
