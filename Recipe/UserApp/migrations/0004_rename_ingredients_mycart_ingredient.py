# Generated by Django 4.1.5 on 2023-03-04 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_remove_mycart_cakes_mycart_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mycart',
            old_name='ingredients',
            new_name='ingredient',
        ),
    ]
