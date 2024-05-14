from django.urls import path, re_path

from ..views.views_equipment import Equipment_Request, Equipment_ID

app_name = "equipment"

urlpatterns = [
    path('', Equipment_Request.as_view({'get': 'get', 'post': 'post'}, name='equipment_request')),
    path('<int:id>', Equipment_ID.as_view({'get': 'get', 'put': 'put', 'delete': 'delete'}, name='equipment_id')),
]
