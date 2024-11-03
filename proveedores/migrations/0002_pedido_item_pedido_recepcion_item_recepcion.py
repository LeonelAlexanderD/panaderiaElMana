# Generated by Django 5.1.2 on 2024-11-03 01:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0001_initial"),
        ("proveedores", "0001_initial"),
        ("usuarios", "0002_empleado_estado"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_pedido", models.DateField(default=datetime.date.today)),
                ("observacion", models.TextField(blank=True)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Pendiente", "Pendiente"),
                            ("Recibido", "Recibido"),
                            ("Cancelado", "Cancelado"),
                        ],
                        default="Pendiente",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proveedores.proveedor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item_Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.PositiveSmallIntegerField()),
                (
                    "insumo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.insumo",
                    ),
                ),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items_pedido",
                        to="proveedores.pedido",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recepcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_recepcion", models.DateField(default=datetime.date.today)),
                ("conformidad", models.TextField()),
                ("observacion", models.TextField(blank=True)),
                (
                    "empleado_receptor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.empleado",
                    ),
                ),
                (
                    "pedido",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proveedores.pedido",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item_Recepcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad_recibida", models.PositiveSmallIntegerField()),
                (
                    "precio_unitario",
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                ("precio_total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "insumo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.insumo",
                    ),
                ),
                (
                    "recepcion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items_recibido",
                        to="proveedores.recepcion",
                    ),
                ),
            ],
        ),
    ]