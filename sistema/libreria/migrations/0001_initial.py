# Generated by Django 3.2.8 on 2021-12-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),

                ('abstract', models.TextField(null=True)),
                ('stock_actual', models.IntegerField(blank=True, null=True)),
                ('stock_total', models.IntegerField(blank=True, null=True)),
                ('fecha_publicacion', models.DateField()),
                ('numero_paginas', models.IntegerField(blank=True, null=True)),
                ('editorial',models.TextField(max_length=900)),





                ('codigo', models.TextField(null=True, verbose_name='Codigo')),
            ],
        ),
    ]
