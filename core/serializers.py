from rest_framework import serializers # type: ignore
from .models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, UnidadMedida, Item, Catalogo05TiposTributos, ItemImpuesto, Categoria
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

    def upload_image_to_s3(self, image):
        # Generate S3 client
        s3 = boto3.client(
            's3',
            region_name=settings.AWS_S3_REGION_NAME
        )
        
        # Define S3 upload parameters
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        file_name = f"items/{image.name}"  # You can customize the file path here
        
        # Upload the image to S3
        s3.upload_fileobj(image, bucket_name, file_name)
        
        # Generate the S3 URL
        file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        
        return file_url

    def create(self, validated_data):
        # Check if image is provided
        image = validated_data.pop('imagen', None)
        
        # If image is present, upload to S3 and get the URL
        if image:
            image_url = self.upload_image_to_s3(image)
            validated_data['imagen'] = image_url  # Store the S3 URL as 'imagen'
        
        # Create the Item instance
        item = Item.objects.create(**validated_data)
        return item

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