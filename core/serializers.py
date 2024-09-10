from rest_framework import serializers # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, Catalogo05TiposTributos, ItemImpuesto

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