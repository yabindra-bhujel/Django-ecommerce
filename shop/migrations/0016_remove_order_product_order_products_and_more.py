# Generated by Django 4.1.7 on 2023-04-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orderitem_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shop.product'),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]
