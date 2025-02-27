# Generated by Django 5.1 on 2024-09-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0002_alter_cliente_nacimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='deporte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='edad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='pais',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='atletas',
        ),
    ]
