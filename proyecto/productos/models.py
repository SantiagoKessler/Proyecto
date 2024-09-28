from django.db import models

class ProductoCategoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'


class Producto(models.Model):
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='categoria')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    unidad_de_medida = models.CharField(max_length=50)
    stock = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre}({self.unidad_de_medida}) ${self.precio:.2f}'
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ('categoria', 'nombre')