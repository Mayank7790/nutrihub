# Generated by Django 4.0.6 on 2022-08-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_product_image_products_product_image_black_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image_black',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_blue',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_grey',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_maroon',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_navy',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_red',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_white',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image_yellow',
            field=models.ImageField(default='null', upload_to='shop/images'),
        ),
    ]