# Generated by Django 5.0.6 on 2024-10-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
