from django.db import models

# Create your models here.

class SegmentoProducto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'segmento_producto'
    
    def __str__(self):
        return self.descripcion
    
class FamiliaProducto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    segmento = models.ForeignKey(SegmentoProducto, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'familia_producto'
    
    def __str__(self):
        return self.descripcion
    
class ClaseProducto(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    familia = models.ForeignKey(FamiliaProducto, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'clase_producto'
    
    def __str__(self):
        return self.descripcion
    
class Producto(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    clase = models.ForeignKey(ClaseProducto, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'producto'
    
    def __str__(self):
        return self.descripcion
    
class TipoPrecio(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'tipo_precio'
    
    def __str__(self):
        return self.descripcion
    
class UnidadMedida(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)  # Unique code for the unit of measure
    descripcion = models.CharField(max_length=200, blank=True, null=True)  # Description of the unit

    class Meta:
        db_table = 'unidad_medida'
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
class Item(models.Model):
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(max_length=200, null=True)
    valorUnitario = models.IntegerField(null=False)
    codigoProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.nombre