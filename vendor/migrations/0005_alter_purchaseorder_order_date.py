# Generated by Django 4.1.13 on 2024-05-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "vendor",
            "0004_rename_filfillment_rate_historicalperformance_fulfilement_rate",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder",
            name="order_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]