from django.forms import ValidationError
from AppUno.models import *


class MaxSizeFileValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 104876

        if size > max_size:
            raise ValidationError(
                f"El tamaño maximo del archivo debe ser de {self.max_file_size} MB")

        return value
