# Generated by Django 4.2.1 on 2023-06-18 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_producto_descripcion_prod_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(db_column='idTipoProducto', default=100, primary_key=True, serialize=False)),
                ('tipoProducto', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='a_materno',
            new_name='apellidos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='a_paterno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='p_nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='s_nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo_producto',
            field=models.ForeignKey(db_column='idTipoProducto', default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.tipoproducto'),
            preserve_default=False,
        ),
    ]