# Generated by Django 5.1 on 2024-09-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0003_pais_altura_pais_deporte_pais_descripcion_pais_edad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='apellido',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
