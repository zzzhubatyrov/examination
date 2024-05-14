from django.contrib import admin
from django.urls import path, re_path, include
from apps.user import views as u_views
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from django.urls import path


schema_view = get_schema_view(
   openapi.Info(
      title="HELPDESK API",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("apps.user.urls")),
    path('api/taskpage/', include("apps.taskpage.urls")),
    path('api/kpp/', include("apps.kpp.urls.urls_kpp")),
    path('api/consignee/', include("apps.kpp.urls.urls_consignee")),
    path('api/delivery/', include("apps.kpp.urls.urls_delivery")),
    path('api/equipment/', include("apps.kpp.urls.urls_equipment")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
