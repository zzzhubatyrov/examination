from ..models.models_delivery import Delivery_Model, Supplier
from rest_framework import serializers


class Supplier_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name',)


class Delivery_Supplier_Serializer(serializers.ModelSerializer):
    name = Supplier_Serializer(many=False)
    class Meta:
        model = Delivery_Model
        fields = ('id', 'name', 'who_pays', 'postal_code', 'region', 'city', 'address', 'middle_name', 'first_name', 'last_name', 'phone', 'email',)
        

class Delivery_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Model
        fields = ('name', 'who_pays', 'postal_code', 'region', 'city', 'address', 'middle_name', 'first_name', 'last_name', 'phone', 'email',)