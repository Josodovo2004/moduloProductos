import csv
from django.core.management.base import BaseCommand
from core.models import SegmentoProducto, FamiliaProducto, ClaseProducto, Producto

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Load SegmentoProducto
        with open('core/management/commands/csv/segmentos.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SegmentoProducto.objects.get_or_create(codigo=row['CODIGO DE SEGMENTO'], descripcion=row['DESCRIPCION DE SEGMENTO'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded SegmentoProducto data.'))

        # Load FamiliaProducto
        with open('core/management/commands/csv/familias.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                segmento = SegmentoProducto.objects.get(codigo=row['CODIGO DE SEGMENTO'])
                FamiliaProducto.objects.get_or_create(codigo=row['CODIGO DE FAMILIA'], segmento=segmento, descripcion=row['DESCRIPCION DE FAMILIA'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded FamiliaProducto data.'))

        # Load ClaseProducto
        with open('core/management/commands/csv/clases.csv', newline='', encoding='windows-1252') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                familia = FamiliaProducto.objects.get(codigo=row['CODIGO DE FAMILIA'])
                ClaseProducto.objects.get_or_create(codigo=row['CODIGO DE CLASE'], familia=familia, descripcion=row['DESCRIPCION DE CLASE'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded ClaseProducto data.'))

        # Load Producto
        with open('core/management/commands/csv/productos.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                clase = ClaseProducto.objects.get(codigo=row['CODIGO DE CLASE'])
                Producto.objects.get_or_create(codigo=str(row['CODIGO DE PRODUCTO']).split('-')[0], clase=clase, descripcion=row['DESCRPCION DE PRODUCTO'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded Producto data.'))
