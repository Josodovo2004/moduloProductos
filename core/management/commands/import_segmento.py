import csv
from django.core.management.base import BaseCommand
from core.models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Load SegmentoProducto
        with open('csv/secmentos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SegmentoProducto.objects.get_or_create(codigo=row['CODIGO DE SEGMENTO'], descripcion=row['DESCRIPCION DE SEGMENTO'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded SegmentoProducto data.'))

        # Load FamiliaProducto
        with open('csv/familias.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                segmento = SegmentoProducto.objects.get(codigo=row['CODIGO DE SEGMENTO'])
                FamiliaProducto.objects.get_or_create(codigo=row['CODIGO DE FAMILIA'], segmento=segmento, descripcion=row['DESCRIPCION DE FAMILIA'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded FamiliaProducto data.'))

        # Load ClaseProducto
        with open('csv/clases.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                familia = FamiliaProducto.objects.get(codigo=row['CODIGO DE FAMILIA'])
                ClaseProducto.objects.get_or_create(codigo=row['CODIGO DE CLASE'], familia=familia, descripcion=row['DESCRIPCION DE CLASE'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded ClaseProducto data.'))

        # Load Producto
        with open('csv/productos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                clase = ClaseProducto.objects.get(codigo=row['CODIGO DE CLASE'])
                Producto.objects.get_or_create(codigo=str(row['CODIGO DE PRODUCTO']).split('-')[0], clase=clase, descripcion=row['DESCRPCION DE PRODUCTO'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded Producto data.'))
