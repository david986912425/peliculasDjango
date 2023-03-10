# Generated by Django 4.0.5 on 2022-08-04 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0007_alter_genero_pelicula'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='id',
            new_name='idmovie',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='id',
        ),
        migrations.RemoveField(
            model_name='genero',
            name='pelicula',
        ),
        migrations.AddField(
            model_name='movie',
            name='genero',
            field=models.ManyToManyField(blank=True, through='Sistema.GeneroMovie', to='Sistema.genero'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='idgenero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.TextField(null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='generomovie',
            name='idgenero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sistema.genero'),
        ),
        migrations.AddField(
            model_name='generomovie',
            name='idmovie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sistema.movie'),
        ),
    ]
