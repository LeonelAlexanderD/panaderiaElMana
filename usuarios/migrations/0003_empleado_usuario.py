# Generated by Django 5.1.2 on 2024-11-04 18:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0002_empleado_estado"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="empleado",
            name="usuario",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="empleado",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
