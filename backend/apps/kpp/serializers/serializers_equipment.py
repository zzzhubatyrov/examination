from ..models.models_equipment import Equipment_Model
from rest_framework import serializers
from django.utils.text import gettext_lazy as _



class Equipment_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment_Model
        fields = '__all__'

