# Generated by Django 3.1.1 on 2020-09-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='servicoOferecido',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
