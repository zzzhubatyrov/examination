from rest_framework.permissions import BasePermission



class KPPPermissions(BasePermission):
    def has_permission(self, request, user):
        if request.user.groups.filter(name='kpp_role') or request.user.is_superuser == True:
            return True
        else:
            return False

