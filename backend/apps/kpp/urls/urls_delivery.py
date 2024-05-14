from django.urls import path, re_path

from ..views.views_delivery import Delivery_Request, Delivery_ID

app_name = "delivery"

urlpatterns = [
    path('', Delivery_Request.as_view({'get': 'get', 'post': 'post'}, name='delivery_request')),
    path('<int:id>', Delivery_ID.as_view({'get': 'get', 'put': 'put', 'delete': 'delete'}, name='delivery_id')),
]
