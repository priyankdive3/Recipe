# Generated by Django 4.1.5 on 2023-02-26 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_remove_category_image_product_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]
