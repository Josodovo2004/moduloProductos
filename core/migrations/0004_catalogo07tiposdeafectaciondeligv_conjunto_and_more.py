# Generated by Django 4.2.16 on 2024-10-29 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_catalogo05tipostributos_un_ece_5153_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo07TiposDeAfectacionDelIGV',
            fields=[
                ('codigo', models.CharField(db_column='Codigo', max_length=2, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Conjunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('fechaLimite', models.DateField(null=True)),
                ('imagen', models.CharField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConjuntoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadItem', models.IntegerField()),
                ('conjunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conjunto')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
        migrations.AddField(
            model_name='itemimpuesto',
            name='afectacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.catalogo07tiposdeafectaciondeligv'),
        ),
    ]
