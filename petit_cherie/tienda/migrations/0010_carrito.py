# Generated by Django 4.2.2 on 2023-06-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_alter_producto_nombre_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('cantidadProducto', models.IntegerField()),
            ],
        ),
    ]
