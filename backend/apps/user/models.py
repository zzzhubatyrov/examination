"""Models for drf-user"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import gettext_lazy as _
from .managers import UserManager

class Role(Group):
    class Meta:
        proxy = True
        verbose_name = _("Роль")
        verbose_name_plural = _("Роли")
        


class Custom_User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_("Имя"), max_length=50, blank=True)
    middle_name = models.CharField(verbose_name=_("Фамилия"), max_length=50, blank=True)
    last_name = models.CharField(verbose_name=_("Отчество"), max_length=50, blank=True)
    username = models.CharField(verbose_name=_("Логин"), max_length=254, unique=True)
    email = models.EmailField(verbose_name=_("Email Address"), blank=True)
    office_phone = models.IntegerField(verbose_name=_("Номер офисного телефона"), null=True, blank=True)
    mobile_phone = models.CharField(verbose_name=_("Номер мобильного телефона"), max_length=20, null=True, blank=True)
    telegram = models.CharField(verbose_name=_("Телеграм"), max_length=50, null=True, blank=True)
    department = models.ForeignKey("Departments", on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(verbose_name=_("Profile Photo"), upload_to="user_images", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name=_("Date Joined"), auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=_("Date Modified"), auto_now=True)
    is_active = models.BooleanField(verbose_name=_("Activated"), default=False)
    is_staff = models.BooleanField(verbose_name=_("Staff Status"), default=False)
    groups = models.ManyToManyField(Role, related_name="groups", blank=True, default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "middle_name", "last_name"]

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    # def get_full_name(self) -> str:
    #     """Method to return user's full name"""

    #     return str(self.name)

    def __str__(self):
        """String representation of model"""

        return str(self.middle_name) + " " + str(self.first_name) + " " + str(self.last_name)


class AuthTransaction(models.Model):
    """
    Represents all authentication in the system that took place via
    REST API.

    Author: Himanshu Shankar (https://himanshus.com)
    """

    ip_address = models.GenericIPAddressField(blank=False, null=False)
    token = models.TextField(verbose_name=_("JWT Access Token"))
    session = models.TextField(verbose_name=_("Session Passed"))
    refresh_token = models.TextField(blank=True,verbose_name=_("JWT Refresh Token"),)
    expires_at = models.DateTimeField(blank=True, null=True, verbose_name=_("Expires At"))
    create_date = models.DateTimeField(verbose_name=_("Create Date/Time"), auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=_("Date/Time Modified"), auto_now=True)
    created_by = models.ForeignKey(to=Custom_User, on_delete=models.PROTECT)

    def __str__(self):
        """String representation of model"""

        return str(self.created_by.first_name) + " | " + str(self.created_by.username)

    class Meta:
        verbose_name = _("Authentication Transaction")
        verbose_name_plural = _("Authentication Transactions")



class Departments(models.Model):
    department = models.CharField("Отдел", max_length=50, null=True)

    def __str__(self):
        return self.department
    
    class Meta:
        verbose_name = _("Отдел")
        verbose_name_plural = _("Отделы")



# class Posts(models.Model):
#     post = models.CharField("Должность", max_length=50, null=True)

#     def __str__(self):
#         return self.post
    
#     class Meta:
#         verbose_name = _("Должность")
#         verbose_name_plural = _("Должности")