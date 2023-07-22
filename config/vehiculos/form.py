from django.forms import ModelForm
from .models import vehiculos


class CrearForm(ModelForm):
    class Meta:
        model = vehiculos
        fields = ['marca', 'modelo', 'serie_carroceria','serie_motor','categoria','precio' ]

        