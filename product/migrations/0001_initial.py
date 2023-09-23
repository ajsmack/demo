# Generated by Django 4.2.5 on 2023-09-23 08:35

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('category_id', models.CharField(default=product.models.get_uuid, max_length=250, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.CharField(default=product.models.get_uuid, max_length=250, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categorymodel')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]