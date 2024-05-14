from django.contrib.auth.password_validation import validate_password
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import CharField
from .models import *



class User_Role(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)



class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department',)



class UserSerializer(serializers.ModelSerializer):
    """
    UserRegisterSerializer is a model serializer which includes the
    attributes that are required for registering a user.
    """

    def validate_password(self, value: str) -> str:
        """Validate whether the password meets all django validator requirements."""
        validate_password(value)
        return value
    
    groups = User_Role(many=True)
    department = DepartmentsSerializer(many=False)

    class Meta:
        """Passing model metadata"""

        model = Custom_User
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "username",
            "email",
            "mobile_phone",
            "office_phone",
            "telegram",
            "department",
            "profile_image",
            "password",
            "is_superuser",
            "is_staff",
            "groups",
        )
        read_only_fields = ("is_superuser", "is_staff", "department")
        extra_kwargs = {"password": {"write_only": True}}









class CheckUniqueSerializer(serializers.Serializer):
    """
    This serializer is for checking the uniqueness of
    username/email/mobile of user.
    """

    prop = serializers.ChoiceField(choices=("email", "mobile_mobile", "office_phone", "username"))
    value = serializers.CharField()



class Login_user(serializers.ModelSerializer):
    username = CharField(required=True)
    password = CharField(required=True)

    class Meta:
        model = Custom_User
        fields = ('username', 'password',)


class User_put(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ("first_name", "middle_name", "last_name", "username",
                  "email", "mobile_phone", "office_phone", "telegram",
                  "department", "profile_image", "is_superuser", "is_staff", "groups",)
        
        read_only_fields = ("is_superuser", "is_staff", "departement", "groups")



class User_Search_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ('id', 'middle_name', 'first_name', 'last_name')
        
        

