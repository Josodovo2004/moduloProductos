from rest_framework import generics # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, ItemImpuesto, Categoria, ConjuntoItem, Conjunto, Catalogo05TiposTributos
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
    ConjuntoItemSerializer,
    ConjuntoSerializer,
    ModifiedItemImpuestoSerializer,
    Catalogo05TiposTributosSerializer,
)
from ModuloProductos.decorators import CustomJWTAuthentication
from ModuloProductos.decorators import jwt_required
from .filters import (
    SegmentoProductoFilter, 
    FamiliaProductoFilter, 
    ClaseProductoFilter, 
    ProductoFilter, 
    ItemFilter, 
    ConjuntoFilter, 
    ConjuntoItemFilter, 
    UnidadMedidaFilter, 
    CategoriaFilter,
    ItemImpuestoFilter,
    )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view # type: ignore
import json
from rest_framework.response import Response
from rest_framework import status
import boto3
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema # type: ignore
from drf_yasg import openapi # type: ignore
from django.shortcuts import get_object_or_404


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = UnidadMedidaFilter
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
    
class CustomItemListView(generics.ListAPIView):  # Change to ListAPIView for list functionality
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter
    
    def get_queryset(self):
        # Get `ids` from query params
        ids = self.request.query_params.get('ids')
        if ids:
            ids = ids.split(',')
            return self.queryset.filter(id__in=ids)
        return self.queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data
        for i in range(len(data['results'])):
            if isinstance(data['results'][i], dict) and 'id' in data['results'][i]:
                item = self.get_queryset().filter(id=data['results'][i]['id']).first()
                if item:
                    data['results'][i]['unidadMedida'] = UnidadMedidaSerializer(item.unidadMedida).data
                    data['results'][i]['tipoPrecio'] = TipoPrecioSerializer(item.tipoPrecio).data
                    data['results'][i]['categoria'] = CategoriaSerializer(item.categoria).data
                    data['results'][i]['codigoProducto'] = ProductoSerializer(item.codigoProducto).data
                    
                    listaImpuestos = ItemImpuesto.objects.filter(item=item.id)
                    if listaImpuestos:
                        serializedImpuestos = ModifiedItemImpuestoSerializer(listaImpuestos, many=True).data
                        data['results'][i]['taxes'] = serializedImpuestos
                 
        response.data = data
        return Response(response.data)

                    

class Catalogo05ListView(generics.ListAPIView):
    queryset = Catalogo05TiposTributos.objects.all()
    serializer_class = Catalogo05TiposTributosSerializer
    


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemImpuestoFilter

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
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoriaFilter


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
    
# List and Create view for Conjunto
class ConjuntoListCreateView(generics.ListCreateAPIView):
    queryset = Conjunto.objects.all()
    serializer_class = ConjuntoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConjuntoFilter
    
    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# Retrieve, Update, and Delete view for Conjunto
class ConjuntoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conjunto.objects.all()
    serializer_class = ConjuntoSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    @jwt_required
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @jwt_required
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# List and Create view for ConjuntoItem
class ConjuntoItemListCreateView(generics.ListCreateAPIView):
    queryset = ConjuntoItem.objects.all()
    serializer_class = ConjuntoItemSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConjuntoItemFilter
    
    @jwt_required
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# Retrieve, Update, and Delete view for ConjuntoItem
class ConjuntoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConjuntoItem.objects.all()
    serializer_class = ConjuntoItemSerializer
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
    
@api_view(['POST'])
def ajustarStock(request):
    try:
        # Get data from the request
        item_id = request.data.get('item_id')
        cantidad = request.data.get('cantidad')

        # Validate that the necessary data is provided
        if item_id is None or cantidad is None:
            return Response({'error': 'Item ID y cantidad son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the item or return 404 if it does not exist
        item = get_object_or_404(Item, id=item_id)

        # Adjust the stock
        item.stock += cantidad  # Increase or decrease the stock
        item.save()  # Save the updated item

        # Return the updated item data
        return Response({
            'id': item.id,
            'nombre': item.nombre,
            'stock': item.stock
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GeneratePresignedUrlView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []

    
    @swagger_auto_schema(
        operation_description="Generate a presigned URL to upload a file to S3. If a file with the same name exists, it will be deleted before generating the URL.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['file_name', 'file_type'],
            properties={
                'file_name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The name of the file to be uploaded to S3."
                ),
                'file_type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="The MIME type of the file (e.g., image/png, application/pdf)."
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Presigned URL generated successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'url': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The generated presigned URL for file upload."
                        ),
                        'file_name': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="The name of the file to be uploaded."
                        ),
                    }
                )
            ),
            400: openapi.Response(
                description="Bad Request. Missing file name or file type.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the issue."
                        )
                    }
                )
            ),
            500: openapi.Response(
                description="Server Error. Could not check file existence or generate presigned URL.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message describing the server error."
                        )
                    }
                )
            ),
        }
    )
    @jwt_required
    def post(self, request):
        file_name = request.data.get('file_name')
        file_type = request.data.get('file_type')

        if not file_name or not file_type:
            return Response({'error': 'File name and file type are required.'}, status=status.HTTP_400_BAD_REQUEST)

        s3_client = boto3.client(
            's3',
            region_name='us-east-1'
        )

        bucket_name = 'qickartbucket'

        # Check if the file exists
        try:
            s3_client.head_object(Bucket=bucket_name, Key=file_name)
            # If it exists, delete the file
            s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        except s3_client.exceptions.ClientError as e:
            if e.response['Error']['Code'] != '404':
                # If the error is something other than "404 Not Found," return an error
                return Response({'error': 'An error occurred while checking for file existence.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Generate the presigned URL for uploading
        try:
            presigned_url = s3_client.generate_presigned_url(
                'put_object',
                Params={
                    'Bucket': bucket_name,
                    'Key': file_name,
                    'ContentType': file_type
                },
                ExpiresIn=120  # URL expiration in seconds
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'url': presigned_url,
            'file_name': file_name
        }, status=status.HTTP_200_OK)