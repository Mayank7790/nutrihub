# Generated by Django 4.1.7 on 2023-03-31 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_products_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=1, max_length=20),
        ),
    ]