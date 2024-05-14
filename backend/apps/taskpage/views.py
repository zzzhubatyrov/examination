from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import *
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters
from rest_framework.decorators import action, api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from backend.__init__ import Custom_Pagination 
from . import TasksPermissions
from django.utils import timezone



class Task_methods(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (TasksPermissions, IsAdminUser,)
    pagination_class = Custom_Pagination
    parser_classes = (MultiPartParser, FormParser,)

    viewset_serializers = {
    'get' : GetTaskSerializer,
    'post' : PostTaskSerializer
}

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request):
        data = Tasks.objects.all().order_by('id')
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Task_id(GenericViewSet):
    renderer_classes=(JSONRenderer,)
    permission_classes=(TasksPermissions, IsAdminUser,)

    viewset_serializers = {
    'get' : GetTaskSerializer,
    'put' : TasksSerializer,
    'delete': TasksSerializer
}
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def put(self, request, id):
        try:
            tasks = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(tasks, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, id):
        try:
            tasks = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def get(self, request, id):
        try:
            tasks = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(tasks, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status==status.HTTP_404_NOT_FOUND)
        



class Task_me(GenericViewSet, ListModelMixin):
    renderer_classes = (JSONRenderer,)
    permission_classes = (TasksPermissions, IsAdminUser,)

    viewset_serializers = {
        'get' : GetTaskSerializer}

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request, parameter = None):
        service = request.query_params.get('service', None)
        task_list = request.query_params.get('task_list', None)

        if service:
            data = Tasks.objects.filter(Q(applicant=request.user.id) | Q(appointed=request.user.id) |
                                        Q(spectator=request.user.id), service__icontains=service).order_by('id').distinct()
            page = self.paginate_queryset(data)
            serializer = self.get_serializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)

        if task_list:
            data = Tasks.objects.filter(Q(applicant=request.user.id) | Q(appointed=request.user.id) |
                                        Q(spectator=request.user.id)).order_by(task_list).distinct()
            page = self.paginate_queryset(data)
            serializer = self.get_serializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)
        
        data = Tasks.objects.filter(Q(applicant=request.user.id) | Q(appointed=request.user.id) |  Q(spectator=request.user.id)).order_by('id').distinct()
        page = self.paginate_queryset(data)
        serializer = self.get_serializer(page, context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)
    



class Facilities_request(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (TasksPermissions, IsAdminUser,)
    viewset_serializers = {
        'get': FacilitiesSerializer
    }

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)

    def get(self, request):
        data = Facilities.objects.all()
        serializer = self.get_serializer(data, context ={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
class Task_Search(ModelViewSet, GenericViewSet):
    queryset = Tasks.objects.all()
    permission_classes = (TasksPermissions, IsAdminUser,)
    serializer_class = GetTaskSerializer
    # filters.SearchFilter, filters.OrderingFilter, 
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    """указывается поиск по элементам определенных строк (SELECT * FROM %field_name% WHERE %query_param% LIKE %query_param% IN %field_name%)""" 
    search_fields = ['service', 'name',]
    """указывается поиск по элементам определенных строк (SELECT * FROM %field_name% WHERE %query_param% EXACT %query_param% IN %field_name%)    """
    filterset_fields = ['service', 'name',]
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return GetTaskSerializer  # Use GetTaskSerializer for GET requests
    #     else:
    #         return TasksSerializer  # Use TaskSerializer for other requests


