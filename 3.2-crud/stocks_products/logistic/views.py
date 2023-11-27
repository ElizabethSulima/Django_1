from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Product, Stock, StockProduct
from .serializers import ProductSerializer, StockSerializer, StockProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['related_name', ]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['related_name', 'description']


class StockProductFilter(filters.FilterSet):
    class Meta:
        model = StockProduct
        fields = ('product__category', 'product__in_stock')

class StockProductListView(generics.ListAPIView):
    queryset = StockProduct.objects.all()
    serializer_class = StockProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockProductFilter

