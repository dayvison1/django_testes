# Generated by Django 3.1.1 on 2020-09-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='horarios',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
    ]
