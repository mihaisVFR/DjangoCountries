# Generated by Django 4.2.1 on 2023-05-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_country_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(to='myapp.language'),
        ),
    ]
