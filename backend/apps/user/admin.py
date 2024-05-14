from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.text import gettext_lazy as _

from .models import Role, Custom_User, Departments


class DRFUserAdmin(UserAdmin):
    """
    Overrides UserAdmin to show fields name & mobile and remove fields:
    first_name, last_name
    """

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Персональная информация"), {"fields": ("middle_name", "first_name", "last_name", "department", "profile_image")}),
        (
            _("Разрешения"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Важные даты"),
            {"fields": ("last_login", "date_joined", "update_date")},
        ),
        (
            _("Контактная информация"),
            {"fields": ("email", "mobile_phone", "office_phone", "telegram")}
        )
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "mobile_phone", "password1", "password2"),
            },
        ),
    )
    list_display = ("middle_name",  "first_name", "last_name", "email", "mobile_phone", "office_phone", "telegram", "department", "role")
    
    def role(self, obj):
        return "\n".join([str(role) for role in obj.groups.all()])
    
    search_fields = ("middle_name", "first_name", "last_name", "username", "is_staff" "email", "mobile_phone", "office_phone", "telegram", "department")
    readonly_fields = ("date_joined", "last_login", "update_date")

class AuthTransactionAdmin(admin.ModelAdmin):
    """AuthTransaction Admin"""

    list_display = ("created_by", "ip_address", "create_date")

    def has_add_permission(self, request):
        """Limits admin to add an object."""

        return False

    def has_change_permission(self, request, obj=None):
        """Limits admin to change an object."""

        return False

    def has_delete_permission(self, request, obj=None):
        """Limits admin to delete an object."""

        return False


# UnRegister default Group & register proxy model Role
# This will also remove additional display of application in admin panel.
# Source: https://stackoverflow.com/a/32445368
admin.site.unregister(Group)
admin.site.register(Role, GroupAdmin)

admin.site.register(Custom_User, DRFUserAdmin)
# admin.site.register(AuthTransaction, AuthTransactionAdmin)
admin.site.register(Departments)
