# Generated by Django 5.1 on 2024-09-03 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atletas',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atletas',
            name='pais_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atletas.pais'),
        ),
    ]
