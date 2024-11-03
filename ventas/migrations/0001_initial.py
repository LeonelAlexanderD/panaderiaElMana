# Generated by Django 5.1.2 on 2024-11-03 01:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente_Mayorista",
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
                ("razon_social", models.CharField(max_length=30)),
                ("cuit", models.PositiveSmallIntegerField()),
                ("telefono", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Comprobante",
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
                ("fecha_de_venta", models.DateField(default=datetime.date.today)),
                (
                    "tipo_de_venta",
                    models.CharField(
                        choices=[("contado", "Contado"), ("credito", "Credito")],
                        max_length=15,
                        verbose_name="Tipo de venta",
                    ),
                ),
                (
                    "forma_de_pago",
                    models.CharField(
                        choices=[
                            ("efectivo", "Efectivo"),
                            ("tarjeta", "Tarjeta"),
                            ("transferencia", "Transferencia"),
                        ],
                        max_length=15,
                        verbose_name="Forma de pago",
                    ),
                ),
                (
                    "total_comprobante",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("observacion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CarritoProducto",
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
                ("cantidad", models.DecimalField(decimal_places=2, max_digits=4)),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.producto",
                    ),
                ),
                (
                    "comprobante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ventas.comprobante",
                    ),
                ),
            ],
        ),
    ]