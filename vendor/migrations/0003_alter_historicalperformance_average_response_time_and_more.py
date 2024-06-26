# Generated by Django 4.1.13 on 2024-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0002_alter_purchaseorder_delivery_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="average_response_time",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="filfillment_rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="on_time_delivery_rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="quality_rating_avg",
            field=models.FloatField(default=0),
        ),
    ]
