from rest_framework import serializers
from proyecto_8_app.models import Institucion, Inscritos


class InscritosSerial(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'

class InstitucionesSerial(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
