from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from product.models import ProductModel, CategoryModel
from rest_framework import serializers
from django.db.models import Q


class CategorySer(serializers.Serializer):
    category_name = serializers.CharField(required=True, max_length=150)


class BaseClass:
    model = None
    serializer = None
    post_read_fields = []
    list_read_fields = []
    search_fields = []

    def read_obj(self, obj, fields):
        return {field: getattr(obj, field) for field in fields}

    def get(self, request):

        objects = self.model.objects.filter(Q())

        if self.search_fields:
            search_condition = Q()
            for search_field in self.search_fields:
                value = request.GET.get(search_field)
                if value:
                    search_condition |= Q(**{f"{search_field}__icontains": value})

            objects = objects.filter(search_condition)

        if objects:
            return Response({
                "success": True,
                "data": [
                    self.read_obj(obj, self.list_read_fields) for obj in objects
                ]
            })
        else:
            return Response({"success": False, "error": "Data Not Found!..."})

    def post(self, request):
        data = request.data

        serializer = self.serializer(data=data)

        if serializer.is_valid():
            obj = self.model(**serializer.validated_data)
            obj.save()
            return Response({
                "success": True,
                "data": self.read_obj(obj, self.post_read_fields)
            })
        else:
            return Response({"success": False, "error": serializer.errors})

    def put(self, request):
        return Response({})

    def delete(self, request):
        return Response({})


class CategoryView(ViewSet, BaseClass):
    model = CategoryModel
    serializer = CategorySer
    post_read_fields = ["category_name", "category_id"]
    list_read_fields = ["category_name", "category_id"]

    search_fields = ["category_name"]
