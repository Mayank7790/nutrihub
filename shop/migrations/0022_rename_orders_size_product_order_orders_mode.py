# Generated by Django 4.1.7 on 2023-04-01 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_register_address_register_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_order',
            old_name='Orders_size',
            new_name='Orders_mode',
        ),
    ]
