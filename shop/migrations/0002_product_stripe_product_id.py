# Generated by Django 4.1.4 on 2023-03-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
