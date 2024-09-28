# Generated by Django 5.1 on 2024-09-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0013_alter_pais_grasa_alter_pais_velocidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={},
        ),
        migrations.AlterField(
            model_name='pais',
            name='grasa',
            field=models.CharField(blank=True, choices=[('6-13%', '6-13%'), ('14-17%', '14-17%'), ('18-24%', '18-24%'), ('25% o mas', '25% o mas')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='velocidad',
            field=models.CharField(blank=True, choices=[('4.6 - 4.9 segundos', ' 4.6 - 4.9 segundos'), ('5.0 - 5.3 segundos', '5.0 - 5.3 segundos'), ('5.4 segundos o más', '5.4 segundos o más')], max_length=100, null=True),
        ),
    ]
