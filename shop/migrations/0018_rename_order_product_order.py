# Generated by Django 4.1.7 on 2023-04-01 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_delete_latest_remove_order_alternative_mobile_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Product_order',
        ),
    ]
