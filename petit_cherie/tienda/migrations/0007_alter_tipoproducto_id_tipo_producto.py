# Generated by Django 4.2.1 on 2023-06-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_usuario_apellidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='id_tipo_producto',
            field=models.AutoField(db_column='idTipoProducto', primary_key=True, serialize=False),
        ),
    ]