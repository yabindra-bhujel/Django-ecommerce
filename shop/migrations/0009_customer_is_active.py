# Generated by Django 4.1.7 on 2023-04-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_product_code_number_product_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]