from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from ..serializers.serializers_kpp import GetTaskSerializer, KPPTaskSerializer, KPPSerializer, KPP_Post_Serializer, Equipment_Template_Serializer
from ..models.models_kpp import KPP_Model, Equipment_Template
from django_filters.rest_framework import DjangoFilterBackend
from backend.__init__ import Custom_Pagination 
from ...kpp.__init__ import KPPPermissions
from django.db.models import Q


class KPP_Search(ModelViewSet, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetTaskSerializer
    renderer_classes = (JSONRenderer,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name']
    queryset = KPP_Model.objects.all()



class KPP_ID(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated, IsAdminUser, )
    pagination_class = Custom_Pagination

    viewset_serializers = {
        'get' : KPPTaskSerializer,
        'put': KPPSerializer

        }
    
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request, id):
        try:
            kpp = KPP_Model.objects.get(id=id)
        except KPP_Model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(kpp, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

    def put(self, request, id):
        try:
            data = KPP_Model.objects.get(id=id)
        except KPP_Model.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class KPP_Request(ModelViewSet, GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (KPPPermissions, IsAdminUser)
    pagination_class = Custom_Pagination
    parser_classes = (MultiPartParser,)
    
    viewset_serializers = {
        'get': KPPTaskSerializer,
        'post' : KPP_Post_Serializer}

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)
    
    
    def get(self, request):
        data = KPP_Model.objects.all().order_by('id')
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class KPP_Me(ModelViewSet, GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (KPPPermissions, IsAdminUser,)
    pagination_class = Custom_Pagination
    
    viewset_serializers = {
        'get': KPPTaskSerializer
    }
    
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)
    
    def get(self, request):
        data = KPP_Model.objects.filter((Q(task__applicant=request.user.id) | Q(task__appointed=request.user.id) |
                                        Q(task__spectator=request.user.id)) & Q(status__id=1)).order_by('id').distinct()
        page = self.paginate_queryset(data)
        serializer = self.get_serializer(page, context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)
    
    

class Equipment_Template_Request(ModelViewSet, GenericViewSet):
    permission_classes = (KPPPermissions, IsAdminUser,)
    pagination_class = Custom_Pagination
    
    viewset_serializers = {
        'get': Equipment_Template_Serializer
    }
    
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)
    
    def get(self, request):
        data = Equipment_Template.objects.all().order_by('id')
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
