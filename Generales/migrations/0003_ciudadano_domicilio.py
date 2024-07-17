# Generated by Django 5.0.3 on 2024-04-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Generales', '0002_variante_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, null=True)),
                ('apellido_paterno', models.CharField(max_length=50, null=True)),
                ('apellido_materno', models.CharField(max_length=50, null=True)),
                ('sobrenombre', models.CharField(max_length=50, null=True)),
                ('genero', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO'), ('OTRO', 'OTRO')], max_length=50, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('fecha_de_nacimiento', models.DateField(null=True)),
                ('observaciones', models.TextField(null=True)),
                ('nombre_completo', models.CharField(max_length=500, null=True)),
                ('nombre_completo_sin_acentos', models.CharField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50, null=True)),
                ('numero_exterior', models.CharField(max_length=50, null=True)),
                ('numero_interior', models.CharField(max_length=50, null=True)),
                ('link_maps', models.URLField(max_length=500, null=True)),
                ('domicilio_completo', models.CharField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]