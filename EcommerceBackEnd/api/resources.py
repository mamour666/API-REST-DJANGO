

from tastypie.resources import ModelResource
from .models import Product
from .models import Category
from tastypie.authorization import Authorization
from django.core import serializers


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()






