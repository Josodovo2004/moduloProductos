import csv
from django.core.management.base import BaseCommand
from core.models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto, TipoPrecio, Catalogo05TiposTributos, UnidadMedida
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Load SegmentoProducto
        with open('core/management/commands/csv/segmentos.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not SegmentoProducto.objects.filter(codigo=row['CODIGO DE SEGMENTO']).exists():
                        SegmentoProducto.objects.create(codigo=row['CODIGO DE SEGMENTO'], descripcion=row['DESCRIPCION DE SEGMENTO'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded SegmentoProducto data.'))

        # Load FamiliaProducto
        with open('core/management/commands/csv/familias.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    segmento = SegmentoProducto.objects.get(codigo=row['CODIGO DE SEGMENTO'])
                    if not FamiliaProducto.objects.filter(codigo=row['CODIGO DE FAMILIA']).exists():
                        FamiliaProducto.objects.create(codigo=row['CODIGO DE FAMILIA'], segmento=segmento, descripcion=row['DESCRIPCION DE FAMILIA'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded FamiliaProducto data.'))

        # Load ClaseProducto
        with open('core/management/commands/csv/clases.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    familia = FamiliaProducto.objects.get(codigo=row['CODIGO DE FAMILIA'])
                    if not ClaseProducto.objects.filter(codigo=row['CODIGO DE CLASE']).exists():
                        ClaseProducto.objects.create(codigo=row['CODIGO DE CLASE'], familia=familia, descripcion=row['DESCRIPCION DE CLASE'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded ClaseProducto data.'))

        # Load Producto
        with open('core/management/commands/csv/productos.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    clase = ClaseProducto.objects.get(codigo=row['CODIGO DE CLASE'])
                    codigo_producto = str(row['CODIGO DE PRODUCTO']).split('-')[0]
                    if not Producto.objects.filter(codigo=codigo_producto).exists():
                        Producto.objects.create(codigo=codigo_producto, clase=clase, descripcion=row['DESCRPCION DE PRODUCTO'])
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded Producto data.'))

        # Load TipoPrecio
        with open('core/management/commands/csv/tipo_precios.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not TipoPrecio.objects.filter(codigo=row['CODIGO']).exists():
                        TipoPrecio.objects.create(
                            codigo=row['CODIGO'], 
                            descripcion=row['DESCRIPCION']
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded TipoPrecio data.'))

        with open('core/management/commands/csv/catalogo_05_tipos_tributos.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not Catalogo05TiposTributos.objects.filter(codigo=row['Codigo']).exists():
                        Catalogo05TiposTributos.objects.create(
                            codigo=row['Codigo'],
                            nombre=row['Name'],
                            descripcion=row['Descripcion'],
                            un_ece_5153=row['UN_ECE_5153'],
                            un_ece_5305=row['UN_ECE_5305']
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded Catalogo05TiposTributos data.'))


        with open('core/management/commands/csv/unidad_medida.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if not UnidadMedida.objects.filter(codigo=row['codigo']).exists():
                        UnidadMedida.objects.create(
                            codigo=row['codigo'],
                            descripcion=row['descripcion']
                        )
                except IntegrityError:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully loaded UnidadMedida data.'))