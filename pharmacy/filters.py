import django_filters
from .models import Stock_Category, Product
#creating a class to filter objects from our models
class Product_filter(django_filters.FilterSet):
    #class meta is temporary classused to alter the content of another class

    class Meta:
        model= Product
        fields=['itemName']


class Category_filder(django_filters.FilterSet):
    class meta:
        model= Stock_Category
        fields=['name']        