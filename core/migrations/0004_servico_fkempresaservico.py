# Generated by Django 3.1.1 on 2020-09-24 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200924_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='fkEmpresaServico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.empresa'),
            preserve_default=False,
        ),
    ]