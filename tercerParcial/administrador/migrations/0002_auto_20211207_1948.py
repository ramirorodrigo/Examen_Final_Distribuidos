# Generated by Django 3.2.8 on 2021-12-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ci',
            field=models.CharField(help_text='                  ', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(help_text='                  ', max_length=190, unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='materno',
            field=models.CharField(help_text='                  ', max_length=15),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(help_text='                  ', max_length=20),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='paterno',
            field=models.CharField(help_text='                  ', max_length=15),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ru',
            field=models.CharField(help_text='                  ', max_length=10, unique=True),
        ),
    ]