# Generated by Django 3.1.1 on 2020-09-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_vagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='idVaga',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vagas',
            name='statusVaga',
            field=models.CharField(choices=[('Indisponível', 'Indisponível'), ('Disponível', 'Disponível'), ('Reservado', 'Reservado')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vagas',
            name='servicoCliente',
            field=models.CharField(choices=[('Cabelo Social', 'Cabelo Social'), ('Cabelo Degradê', 'Cabelo Degradê'), ('Barba Simples', 'Barba Simples')], max_length=255),
        ),
    ]
