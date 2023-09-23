from django.db import models
import uuid


def get_uuid(): return str(uuid.uuid4())


class CategoryModel(models.Model):
    category_id = models.CharField(primary_key=True, default=get_uuid, max_length=250)

    category_name = models.CharField(max_length=150)

    class Meta:
        db_table = "category"


class ProductModel(models.Model):
    product_id = models.CharField(primary_key=True, default=get_uuid, max_length=250)

    product_name = models.CharField(max_length=150)
    price = models.FloatField()

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"


class HelloModal(models.Model):
    product_id = models.CharField(primary_key=True, default=get_uuid, max_length=250)

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
