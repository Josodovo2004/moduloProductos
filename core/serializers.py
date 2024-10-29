from rest_framework import serializers # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, Catalogo05TiposTributos, ItemImpuesto, Categoria, Conjunto, ConjuntoItem
import boto3
from django.conf import settings

class SegmentoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegmentoProducto
        fields = '__all__'

class FamiliaProductoSerializer(serializers.ModelSerializer):
    segmento = SegmentoProductoSerializer(read_only=True)

    class Meta:
        model = FamiliaProducto
        fields = '__all__'

class ClaseProductoSerializer(serializers.ModelSerializer):
    familia = FamiliaProductoSerializer(read_only=True)

    class Meta:
        model = ClaseProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    clase = ClaseProductoSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'

class TipoPrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPrecio
        fields = '__all__'

class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(write_only=True, required=False)  # Image field for uploading

    class Meta:
        model = Item
        fields = '__all__'

class Catalogo05TiposTributosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo05TiposTributos
        fields = '__all__'


class ItemImpuestoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemImpuesto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
        
class ConjuntoItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)  # Nesting Item serializer to get all item details
    
    class Meta:
        model = ConjuntoItem
        fields = ['id', 'item', 'cantidadItem']

class ConjuntoSerializer(serializers.ModelSerializer):
    conjuntoitem_set = ConjuntoItemSerializer(many=True, read_only=True)  # Nesting ConjuntoItem serializer

    class Meta:
        model = Conjunto
        fields = ['id', 'precio', 'fechaLimite', 'imagen', 'conjuntoitem_set']