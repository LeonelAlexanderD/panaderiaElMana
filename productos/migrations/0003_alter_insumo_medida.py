# Generated by Django 5.1.2 on 2024-11-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0002_alter_producto_precio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="insumo",
            name="medida",
            field=models.CharField(
                choices=[("unidad", "u."), ("gramo", "gr."), ("kilogramo", "kg.")],
                max_length=30,
            ),
        ),
    ]