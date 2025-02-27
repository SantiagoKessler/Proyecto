# Generated by Django 5.1 on 2024-09-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0010_pais_test_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='test_speed',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='nivel',
        ),
        migrations.AddField(
            model_name='pais',
            name='edad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='deporte',
            field=models.CharField(blank=True, choices=[('F', 'Futbol'), ('R', 'Rugby'), ('B', 'Basquet'), ('T', 'Tenis'), ('A', 'Atletismo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='grasa',
            field=models.CharField(blank=True, choices=[('6-13%', '6-13%'), ('14-17%', '14-17%'), ('18-24%', '18-24%'), ('25% o mas', '25% o mas')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='TestSpeed',
        ),
    ]
