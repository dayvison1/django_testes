# Generated by Django 3.1.1 on 2020-09-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_servico_fkempresaservico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(max_length=255)),
                ('telefoneCliente', models.CharField(max_length=255)),
                ('servicoCliente', models.CharField(choices=[('a', 'A'), ('b', 'B')], max_length=255)),
            ],
        ),
    ]
