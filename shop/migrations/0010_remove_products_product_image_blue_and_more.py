# Generated by Django 4.1.7 on 2023-03-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_products_product_image_black_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image_blue',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_image_grey',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_image_maroon',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_image_navy',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_image_white',
        ),
    ]