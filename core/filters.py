from django_filters import rest_framework as filters
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, Item, Conjunto, ConjuntoItem, UnidadMedida, Categoria, ItemImpuesto

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
    categoria = filters.CharFilter(field_name='categoria__nombre', lookup_expr='icontains')  # Filter by category name
    unidadMedida = filters.CharFilter(lookup_expr='icontains')  # Filter by unit name
    tipoPrecio = filters.CharFilter(lookup_expr='icontains')  # Filter by price type name
    nombre = filters.CharFilter(lookup_expr='icontains')  # Filter by item name
    valorUnitario_min = filters.NumberFilter(field_name='valorUnitario', lookup_expr='gte')  # Minimum value filter
    valorUnitario_max = filters.NumberFilter(field_name='valorUnitario', lookup_expr='lte')  # Maximum value filter
    stock_min = filters.NumberFilter(field_name='stock', lookup_expr='gte')  # Minimum stock filter
    stock_max = filters.NumberFilter(field_name='stock', lookup_expr='lte')  # Maximum stock filter
    peso_min = filters.NumberFilter(field_name='peso', lookup_expr='gte')  # Minimum weight filter
    peso_max = filters.NumberFilter(field_name='peso', lookup_expr='lte')  # Maximum weight filter
    volumen_min = filters.NumberFilter(field_name='volumen', lookup_expr='gte')  # Minimum volume filter
    volumen_max = filters.NumberFilter(field_name='volumen', lookup_expr='lte')  # Maximum volume filter
    codigoBarras = filters.CharFilter( lookup_expr='icontains')

    class Meta:
        model = Item
        fields = [
            'categoria', 'unidadMedida', 'tipoPrecio', 'nombre',
            'valorUnitario_min', 'valorUnitario_max',
            'stock_min', 'stock_max', 'peso_min', 'peso_max',
            'volumen_min', 'volumen_max', 'codigoBarras'
        ]

class ConjuntoFilter(filters.FilterSet):
    precio_min = filters.NumberFilter(field_name="precio", lookup_expr="gte")
    precio_max = filters.NumberFilter(field_name="precio", lookup_expr="lte")
    fecha_limite = filters.DateFilter(field_name="fechaLimite")

    class Meta:
        model = Conjunto
        fields = ['precio', 'fechaLimite']

class ConjuntoItemFilter(filters.FilterSet):
    cantidad_min = filters.NumberFilter(field_name="cantidadItem", lookup_expr="gte")
    cantidad_max = filters.NumberFilter(field_name="cantidadItem", lookup_expr="lte")
    item_id = filters.NumberFilter(field_name="item__id")

    class Meta:
        model = ConjuntoItem
        fields = ['cantidadItem', 'item']
    
class UnidadMedidaFilter(filters.FilterSet):
    codigo = filters.CharFilter(lookup_expr='icontains')  # Filter by code (partial match)
    descripcion = filters.CharFilter(lookup_expr='icontains')  # Filter by description (partial match)

    class Meta:
        model = UnidadMedida
        fields = ['codigo', 'descripcion']
        
class CategoriaFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nombre']
        
class ItemImpuestoFilter(filters.FilterSet):
    item = filters.NumberFilter(field_name='item__id')  # Filtering by item ID
    impuesto = filters.NumberFilter(field_name='impuesto__id')  # Filtering by impuesto ID
    porcentaje = filters.NumberFilter()  # Exact match for porcentaje
    afectacion = filters.NumberFilter(field_name='afectacion__id')  # Filtering by afectacion ID

    # Filter for NULL values in afectacion
    afectacion_isnull = filters.BooleanFilter(
        field_name='afectacion',
        lookup_expr='isnull',
        label='Afectacion is NULL'
    )

    class Meta:
        model = ItemImpuesto
        fields = ['item', 'impuesto', 'porcentaje', 'afectacion', 'afectacion_isnull']