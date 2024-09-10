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
    
class Catalogo05TiposTributos(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=4, primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Name', max_length=6, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    un_ece_5153 = models.CharField(db_column='UN_ECE_5153', max_length=3, blank=True, null=True)  # Field name made lowercase.
    un_ece_5305 = models.CharField(db_column='UN_ECE_5305', max_length=1, blank=True, null=True)


    class Meta:
        db_table = 'CATALOGO_05_TIPOS_TRIBUTOS'

    def __str__(self) -> str:
        return self.nombre

    
class Item(models.Model):
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    tipoPrecio = models.ForeignKey(TipoPrecio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(max_length=200, null=True)
    valorUnitario = models.IntegerField(null=False)
    codigoProducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, null=True)
    stock = models.IntegerField(null=False)
    peso = models.FloatField(null=True)
    volumen = models.FloatField(null=True) #volumen en metros cubicos

    def __str__(self) -> str:
        return self.nombre
    

class ItemImpuesto(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    impuesto = models.ForeignKey(Catalogo05TiposTributos, on_delete=models.DO_NOTHING)
    porcentaje=models.FloatField(null=False) #0.18 for IGV for example