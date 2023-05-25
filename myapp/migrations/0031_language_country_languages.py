# Generated by Django 4.2.1 on 2023-05-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_remove_country_languages_delete_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(to='myapp.language'),
        ),
    ]
