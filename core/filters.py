from django_filters import rest_framework as filters
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, Item

class SegmentoProductoFilter(filters.FilterSet):
    descripcion = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SegmentoProducto
        fields = ['codigo', 'descripcion']


class FamiliaProductoFilter(filters.FilterSet):
    segmento_codigo = filters.CharFilter(field_name='segmento__codigo', lookup_expr='exact')
    descripcion = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FamiliaProducto
        fields = ['codigo', 'segmento_codigo', 'descripcion']


class ClaseProductoFilter(filters.FilterSet):
    familia_codigo = filters.CharFilter(field_name='familia__codigo', lookup_expr='exact')
    descripcion = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ClaseProducto
        fields = ['codigo', 'familia_codigo', 'descripcion']


class ProductoFilter(filters.FilterSet):
    clase_codigo = filters.CharFilter(field_name='clase__codigo', lookup_expr='exact')
    descripcion = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Producto
        fields = ['codigo', 'clase_codigo', 'descripcion']
        
class ItemFilter(filters.FilterSet):
    categoria = filters.CharFilter(field_name='categoria', lookup_expr='exact')
    class Meta:
        model = Item
        fields = ['categoria']
