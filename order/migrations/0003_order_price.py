# Generated by Django 5.1.1 on 2024-12-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_date_alter_order_payed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
