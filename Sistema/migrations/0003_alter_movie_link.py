# Generated by Django 4.0.5 on 2022-08-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0002_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.CharField(max_length=130, verbose_name='Link'),
        ),
    ]
