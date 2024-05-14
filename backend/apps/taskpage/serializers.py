from .models import *
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from apps.user.models import Custom_User

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
                  'service', 
                  'name', 
                  'description',
                  'facility', 
                  'address', 
                  'applicant', 
                  'tags', 
                  'deadline', 
                  'date_creation',
                  'date_end', 
                  'appointed', 
                  'spectator', 
                  'labor_intensity', 
                  'document', 
                  'status',
                  )



class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('id', 'facility', 'address')



class Documents_Nested(serializers.ListField):
    child = serializers.FileField()
    class Meta:
        model = Documents_templates
        fields = ('document', )


class Documents_templates_serializer(serializers.ModelSerializer):
    document = Documents_Nested()
    class Meta:
        model = Documents_templates
        fields = ['document', ]



class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['id', 'username', 'first_name', 'middle_name', 'last_name']



class GetTaskSerializer(serializers.ModelSerializer):
    appointed = UserTaskSerializer(many=True)
    spectator = UserTaskSerializer(many=True)
    applicant = UserTaskSerializer(many=True)
    # document = Documents_templates_serializer(many=True)
    # document = Documents_templates_serializer()

    class Meta:
        model = Tasks
        fields = (
                  'id',
                  'service',
                  'name', 
                  'description',
                  'facility', 
                  'address', 
                  'applicant', 
                  'tags', 
                  'deadline', 
                  'date_creation',
                  'date_end', 
                  'appointed', 
                  'spectator', 
                  'labor_intensity', 
                  'document', 
                  'status',)



class PostTaskSerializer(serializers.ModelSerializer):
    document = serializers.ListField(child=serializers.FileField(), write_only=True, required=False)
    class Meta:
        model = Tasks
        fields = (
                  'service', 
                  'name', 
                  'description',
                  'facility', 
                  'address', 
                  'applicant', 
                  'tags', 
                  'deadline', 
                  'date_creation',
                  'date_end', 
                  'appointed', 
                  'spectator', 
                  'labor_intensity', 
                  'document', 
                  'status',
                  )
        
    def create(self, validated_data):
        documents_data = validated_data.pop('document', [])
        applicants_data = validated_data.pop('applicant', [])
        spectators_data = validated_data.pop('spectator', [])
        appointeds_data = validated_data.pop('appointed', [])
        task = Tasks.objects.create(**validated_data)
        
        for document_data in documents_data:
            document = Documents_templates.objects.create(document=document_data)
            task.document.add(document)
            
        for applicants_data in applicants_data:
            task.applicant.add(applicants_data)
            
        for spectators_data in spectators_data:
            task.spectator.add(spectators_data)
            
        for appointeds_data in appointeds_data:
            task.appointed.add(appointeds_data)
            
        return task