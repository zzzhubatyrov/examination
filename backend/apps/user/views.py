from django.conf import settings
from django.utils.text import gettext_lazy as _
from django.contrib.auth import authenticate, login
from drfaddons.utils import JsonResponse
from django.db.models.functions import Concat
from django.db.models import Value
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Custom_User
from .serializers import *
from .utils import check_unique
from backend.__init__ import Custom_Pagination
from . import UserPermissions



class RegisterView(CreateAPIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (UserPermissions, IsAdminUser,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        data = {
            "first_name": serializer.validated_data["first_name"],
            "middle_name": serializer.validated_data["middle_name"],
            "last_name": serializer.validated_data["last_name"],
            "username": serializer.validated_data["username"],
            "email": serializer.validated_data["email"],
            "password": serializer.validated_data["password"],
        }
        return Custom_User.objects.create_user(**data)



class login_view(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = Login_user

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            authenticated_user = authenticate(**serializer.validated_data)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return Response({'status': 'Success'})
            else:
                return Response({'error': 'Invalid credentials'}, status=401)
        else:
            return Response(serializer.errors, status=400)



class CheckUniqueView(APIView):
    """
    Check Unique API View

    This view checks if the given property -> value pair is unique (or
    doesn't exists yet)
    'prop' -- A property to check for uniqueness (username/email/mobile)
    'value' -- Value against property which is to be checked for.
    """

    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = CheckUniqueSerializer

    def validated(self, serialized_data, *args, **kwargs):
        """Validates the response"""
        return (
            {
                "unique": check_unique(
                    serialized_data.validated_data["prop"],
                    serialized_data.validated_data["value"],
                )
            },
            status.HTTP_200_OK,
        )

    def post(self, request):
        """Overrides post method to validate serialized data"""
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            return JsonResponse(self.validated(serialized_data=serialized_data))
        else:
            return JsonResponse(
                serialized_data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

class Get_Users(GenericAPIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (UserPermissions, IsAdminUser,)
    serializer_class = UserSerializer
    pagination_class = Custom_Pagination

    def get(self, request, search = None):
        if search is None:
            try:
                data = Custom_User.objects.all()
            except Custom_User.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(data, context={'request': request}, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        data = Custom_User.objects.annotate(name=Concat('first_name', Value(' '), 'middle_name', Value(' '), 'last_name')).filter(name__icontains=search)
        page = self.paginate_queryset(data)
        serializer = self.serializer_class(page, context={'request': request}, many=True)
        return self.get_paginated_response(serializer.data)



class Get_User(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (UserPermissions, IsAdminUser,)
    serializer_class = UserSerializer


    def get(self, request, id):
        try:
            data = Custom_User.objects.filter(id=id)
        except Custom_User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Get_Me(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (UserPermissions, IsAdminUser,)
    viewset_serializers = {
        'get': UserSerializer,
        'put': User_put
    }

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)

    def get(self, request):
        data = Custom_User.objects.get(username=request.user.username)
        serializer = self.get_serializer(data, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        me = Custom_User.objects.get(username=request.user.username)
        serializer = self.get_serializer(me, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)



class Department_Request(GenericViewSet):
    renderer_classes = (JSONRenderer,)
    permission_classes = (UserPermissions, IsAdminUser,)
    viewset_serializers = {
        'get': DepartmentsSerializer
    }

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.viewset_serializers.get(self.action)
        return serializer_class(*args, **kwargs)


    def get(self, request):
        data = Departments.objects.all()
        serializer = self.get_serializer(data, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class Posts_Request(GenericViewSet):
#     renderer_classes = (JSONRenderer,)
#     permission_classes = (UserPermissions, IsAdminUser,)
#     viewset_serializers = {
#         'get': PostsSerializer
#     }

#     def get_serializer(self, *args, **kwargs):
#         serializer_class = self.viewset_serializers.get(self.action)
#         return serializer_class(*args, **kwargs)

    
#     def get(self, request):
#         data = Posts.objects.all()
#         serializer = self.get_serializer(data, context={'request': request}, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    