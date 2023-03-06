# Generated by Django 4.1.5 on 2023-03-04 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_ingredients_quantity'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='mycart',
            name='cakes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.product'),
            preserve_default=False,
        ),
    ]
