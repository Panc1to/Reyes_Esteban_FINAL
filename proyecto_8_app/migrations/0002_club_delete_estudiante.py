# Generated by Django 4.2.6 on 2023-12-23 02:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_8_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombresocio', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(80)])),
                ('fechaincorporación', models.DateField()),
                ('añonacimiento', models.IntegerField()),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('hombre', 'HOMBRE'), ('mujer', 'MUJER'), ('no binario', 'NO BINARIO')], max_length=50)),
                ('estado', models.CharField(choices=[('vigente', 'VIGENTE'), ('suspendido', 'SUSPENDIDO'), ('retirado', 'RETIRADO')], max_length=50)),
                ('observacion', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
