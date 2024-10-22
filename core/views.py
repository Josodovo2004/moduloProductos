from rest_framework import generics # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, ItemImpuesto, Categoria
from .serializers import (
    SegmentoProductoSerializer,
    FamiliaProductoSerializer,
    ClaseProductoSerializer,
    ProductoSerializer,
    TipoPrecioSerializer,
    UnidadMedidaSerializer,
    ItemSerializer,
    ItemImpuestoSerializer,
    CategoriaSerializer,
)
from ModuloProductos.decorators import CustomJWTAuthentication
from ModuloProductos.decorators import jwt_required
from .filters import SegmentoProductoFilter, FamiliaProductoFilter, ClaseProductoFilter, ProductoFilter, ItemFilter
from django_filters.rest_framework import DjangoFilterBackend

class SegmentoProductoListCreateView(generics.ListCreateAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SegmentoProductoFilter
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class SegmentoProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class FamiliaProductoListCreateView(generics.ListCreateAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FamiliaProductoFilter
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class FamiliaProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class ClaseProductoListCreateView(generics.ListCreateAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClaseProductoFilter
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class ClaseProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class ProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class TipoPrecioListCreateView(generics.ListCreateAPIView):
    queryset = TipoPrecio.objects.all()
    serializer_class = TipoPrecioSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class TipoPrecioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPrecio.objects.all()
    serializer_class = TipoPrecioSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class UnidadMedidaListCreateView(generics.ListCreateAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

class UnidadMedidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

# Secure CRUD views for Item
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ItemImpuestoListCreateView(generics.ListCreateAPIView):
    queryset = ItemImpuesto.objects.all()
    serializer_class = ItemImpuestoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ItemImpuestoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemImpuesto.objects.all()
    serializer_class = ItemImpuestoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)