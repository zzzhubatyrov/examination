from ..models.models_consignee import Consignee_Model
from rest_framework import serializers
from django.utils.text import gettext_lazy as _



class Consignee_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Consignee_Model
        fields = '__all__'