from rest_framework import generics # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, ItemImpuesto
from .serializers import (
    SegmentoProductoSerializer,
    FamiliaProductoSerializer,
    ClaseProductoSerializer,
    ProductoSerializer,
    TipoPrecioSerializer,
    UnidadMedidaSerializer,
    ItemSerializer,
    ItemImpuestoSerializer
)

class SegmentoProductoListCreateView(generics.ListCreateAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer

class SegmentoProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer

class FamiliaProductoListCreateView(generics.ListCreateAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer

class FamiliaProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer

class ClaseProductoListCreateView(generics.ListCreateAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer

class ClaseProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoPrecioListCreateView(generics.ListCreateAPIView):
    queryset = TipoPrecio.objects.all()
    serializer_class = TipoPrecioSerializer

class TipoPrecioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPrecio.objects.all()
    serializer_class = TipoPrecioSerializer

class UnidadMedidaListCreateView(generics.ListCreateAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

class UnidadMedidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemImpuestoListCreateView(generics.ListCreateAPIView):
    queryset = ItemImpuesto.objects.all()
    serializer_class = ItemImpuestoSerializer

class ItemImpuestoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemImpuesto.objects.all()
    serializer_class = ItemImpuestoSerializer