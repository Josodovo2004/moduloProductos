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
from rest_framework.decorators import api_view # type: ignore
import json
from rest_framework.response import Response
from rest_framework import status
class SegmentoProductoListCreateView(generics.ListCreateAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SegmentoProductoFilter


class SegmentoProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SegmentoProducto.objects.all()
    serializer_class = SegmentoProductoSerializer


class FamiliaProductoListCreateView(generics.ListCreateAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FamiliaProductoFilter


class FamiliaProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FamiliaProducto.objects.all()
    serializer_class = FamiliaProductoSerializer


class ClaseProductoListCreateView(generics.ListCreateAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClaseProductoFilter


class ClaseProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClaseProducto.objects.all()
    serializer_class = ClaseProductoSerializer


class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter


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
    
@api_view(['POST'])
def resumenItems(request):
    try:
        data = request.data  # No need to use json.loads here
        # You can print or process 'data' here if necessary
        print(data)
        returnData = []
        for value in data:
            id_item = value['codigoItem']
            item = Item.objects.filter(id=id_item).first()
            itemImpuesto = ItemImpuesto.objects.filter(item__id=id_item)
            precioTotal = item.valorUnitario * value['cantidad']
            impuestos = {}
            for impuesto in itemImpuesto:
                if impuesto.impuesto.nombre not in impuestos.keys():
                    impuestos[impuesto.impuesto.nombre] = {
                        'id': impuesto.impuesto.codigo,
                        'name': impuesto.impuesto.nombre,
                        'tax_type_code': impuesto.impuesto.un_ece_5153, 
                        'tax_amount' : (impuesto.porcentaje/100) * precioTotal
                    }
            returnData.append({
                'precioTotal': precioTotal,
                'tax' : impuestos,
            })
        
        # Return a successful response
        return Response(returnData, status=status.HTTP_200_OK)
    
    except Exception as e:
        # Log the error (optional)
        print(f'Error: {e}')
        
        # Return a user-friendly error message
        return Response({'error': 'Something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)