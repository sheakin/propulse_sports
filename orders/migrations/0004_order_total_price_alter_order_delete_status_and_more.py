# Generated by Django 5.0.6 on 2024-08-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_remove_order_total_price_alter_order_delete_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="order",
            name="delete_status",
            field=models.IntegerField(choices=[(1, "Live"), (0, "Delete")], default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.IntegerField(
                choices=[
                    (2, "ORDER_PROCESSED"),
                    (3, "ORDER_DELIVERED"),
                    (4, "ORDER_REJECTED"),
                    (1, "ORDER_CONFIRMED"),
                ],
                default=0,
            ),
        ),
    ]
