from ..models.models_kpp import KPP_Model, KPP_Status, KPP_Documents, Equipment_Template
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from apps.taskpage.serializers import GetTaskSerializer, UserTaskSerializer
from .serializers_delivery import Delivery_Serializer
from .serializers_consignee import Consignee_Serializers
from .serializers_equipment import Equipment_Serializers


class KPPSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPP_Model
        fields = ['name_number', 'name', 'description', 'tin', 'kpp', 'сustomer_contact_person', 'customer_phone',
                  'customer_email', 'consignee_details', 'delivery_method', 'contract', 'bill', 'price', 'payment_terms',
                  'payment_order', 'manager', 'sold_by', 'priority', 'difficulty', 'date_started', 'date_end', 'status', 'document', 'task', 'equipment', ]
        
    

class KPPStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPP_Status
        fields = ('status', )




class KPPTaskSerializer(serializers.ModelSerializer):
    task = GetTaskSerializer(many=True)
    status = KPPStatusSerializer()
    delivery_method = Delivery_Serializer()
    consignee_details = Consignee_Serializers()
    manager = UserTaskSerializer(many=True)
    equipment = Equipment_Serializers(many=True)


    class Meta:
        model = KPP_Model
        fields = ['id', 'name_number', 'name', 'description', 'tin', 'kpp', 'сustomer_contact_person', 'customer_phone',
                  'customer_email', 'consignee_details', 'delivery_method', 'contract', 'bill', 'price', 'payment_terms',
                  'payment_order', 'manager', 'sold_by', 'priority', 'difficulty', 'date_started', 'date_end', 'status', 'document', 'task', 'equipment', ]

        
class KPP_Post_Serializer(serializers.ModelSerializer):
    document = serializers.ListField(child=serializers.FileField(), write_only=True)
    class Meta:
        model = KPP_Model
        fields = ['name_number', 'name', 'description', 'tin', 'kpp', 'сustomer_contact_person', 'customer_phone',
                  'customer_email', 'consignee_details', 'delivery_method', 'contract', 'bill', 'price', 'payment_terms',
                  'payment_order', 'manager', 'sold_by', 'priority', 'difficulty', 'date_started', 'date_end', 'status', 'document', 'task', 'equipment', ]
        
    def create(self, validated_data):
        documents_data = validated_data.pop('document', [])
        managers_data = validated_data.pop('manager', [])
        task_data = validated_data.pop('task', [])
        equipment_data = validated_data.pop('equipment', [])
        kpp = KPP_Model.objects.create(**validated_data)
        
        for document_data in documents_data:
            document = KPP_Documents.objects.create(document=document_data)
            kpp.document.add(document)
            
        for managers_data in managers_data:
            kpp.manager.add(managers_data)    
            
        for task_data in task_data:
            kpp.task.add(task_data)

        for equipment_data in equipment_data:
                    kpp.equipment.add(equipment_data)

        return kpp

class Equipment_Template_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment_Template
        fields = '__all__'

