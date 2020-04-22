from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class AcionamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acionamentos
        fields = '__all__'

class DispositivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivos
        fields = '__all__'        