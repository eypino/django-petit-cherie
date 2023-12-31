# Generated by Django 4.2.2 on 2023-07-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=10)),
                ('fecha_nac', models.DateField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=1)),
            ],
        ),
    ]
