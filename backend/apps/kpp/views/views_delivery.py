from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from ..serializers.serializers_delivery import Delivery_Serializer, Delivery_Supplier_Serializer, Supplier_Serializer
from ..models.models_delivery import Delivery_Model, Supplier
from backend.__init__ import Custom_Pagination 



class Delivery_Request(ModelViewSet, GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = (Delivery_Supplier_Serializer)
    pagination_class = Custom_Pagination
    
    viewset_serializers = {
        'get': Delivery_Supplier_Serializer,
        'post': Delivery_Serializer
    }
    
    
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request):
        data = Delivery_Model.objects.all().order_by('id')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class Delivery_ID(ModelViewSet, GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = (Delivery_Supplier_Serializer)
    
    viewset_serializers = {
        'get':Delivery_Supplier_Serializer,
        'put': Delivery_Serializer,
        'delete': Delivery_Supplier_Serializer
    }
    
    
    def get_serializer(self, *args, **kwargs):
        serlalizer_class = self.viewset_serializers.get(self.action)
        return serlalizer_class(*args, **kwargs)
    
    
    def get(self, request, id):
        try:
            delivery = Delivery_Model.objects.get(id=id)
        except Delivery_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(delivery, data=request.data, context = {'request': request}, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        try:
            delivery = Delivery_Model.objects.get(id=id)
        except Delivery_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(delivery, data=request.data, context = {'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        try:
            delivery = Delivery_Model.objects.get(id=id)
        except Delivery_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        delivery.delete()
        return Response(status=status.HTTP_200_OK)
    
    

class Supplier_Request(ModelViewSet, GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = (Supplier_Serializer)
    viewset_serializers = {
        'get': Supplier_Serializer
    }
    
    
    def get_serializer_class(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)
    
    
    def get(self, request):
        data = Supplier.objects.all().order_by('id')
        serializer = self.get_serializer(data, context = {'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)