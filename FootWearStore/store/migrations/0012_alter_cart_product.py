# Generated by Django 4.0.3 on 2022-04-20 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_product_color_remove_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.size_quantity'),
        ),
    ]
