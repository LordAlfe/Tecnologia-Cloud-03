from django.db import models

# Create your models here.
TIPO = [('RECLAMO', 'reclamo'), ('FELICITACIONES', 'Felicitaciones')]


class Formulario(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    tipo = models.TextField(choices=TIPO)
    descripcion = models.TextField(verbose_name="Descripcion")
    evidencia = models.ImageField(verbose_name="Evidencia")

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'
        db_table = 'form'

    def tipo_form(self):
        return "{}".format(self.tipo)

    def __str__(self):
        return self.tipo_form()
