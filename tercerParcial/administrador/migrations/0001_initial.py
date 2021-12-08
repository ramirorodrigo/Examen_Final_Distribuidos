# Generated by Django 3.2.8 on 2021-12-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introdusca nombre de asignatura', max_length=30)),
                ('sigla', models.CharField(help_text='Introdusca la Sigla', max_length=6, unique=True)),
                ('horas', models.IntegerField(blank=True, null=True)),
                ('semestre', models.IntegerField(help_text='Introdusca el N° semestre')),
            ],
            options={
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introdusca los nombres', max_length=20)),
                ('paterno', models.CharField(help_text='Introdusca el apellido paterno', max_length=15)),
                ('materno', models.CharField(help_text='Introdusca el apellido materno', max_length=15)),
                ('ru', models.CharField(help_text='Introdusca el R.U.', max_length=10, unique=True)),
                ('email', models.EmailField(max_length=190, unique=True)),
                ('ci', models.CharField(help_text='Introdusca el C.I.', max_length=12, unique=True)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'ordering': ['-paterno', 'materno', 'nombre'],
            },
        ),
    ]
