from django.db import models

# Create your models here.
TIPO = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


class Formulario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    rut = models.CharField(verbose_name="Rut", max_length=9)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellido = models.CharField(
        verbose_name="Apellido", max_length=50)
    fecha = models.CharField(verbose_name="Fecha", max_length=10)
    tipo = models.IntegerField(choices=TIPO)
    descripcion = models.TextField(verbose_name="Descripcion")
    # evidencia = models.ImageField(verbose_name="Evidencia")

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'
        db_table = 'form'

    def tipo_form(self):
        return "{}".format(self.tipo)

    def __str__(self):
        return self.tipo_form()
