from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.viewsets import GenericViewSet  
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..serializers.serializers_consignee import Consignee_Serializers
from ..models.models_consignee import Consignee_Model
from backend.__init__ import Custom_Pagination 



class Consignee_Request(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAdminUser, IsAuthenticated, )
    pagination_class = Custom_Pagination

    viewset_serializers = {
    'get' : Consignee_Serializers,
    'post' : Consignee_Serializers
}

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request):
        data = Consignee_Model.objects.all().order_by('id')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        

class Consignee_ID(GenericViewSet):
    renderer_classes=(JSONRenderer,)
    permission_classes=(IsAuthenticated, IsAdminUser,)

    viewset_serializers = {
    'get' : Consignee_Serializers,
    'put' : Consignee_Serializers,
    'delete': Consignee_Serializers
}
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def put(self, request, id):
        try:
            fields = Consignee_Model.objects.get(id=id)
        except Consignee_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(fields, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, id):
        try:
            tasks = Consignee_Model.objects.get(id=id)
        except Consignee_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def get(self, request, id):
        try:
            fields = Consignee_Model.objects.get(id=id)
        except Consignee_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(fields, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status==status.HTTP_404_NOT_FOUND)