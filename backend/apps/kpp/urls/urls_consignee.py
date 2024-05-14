from django.urls import path, re_path

from ..views.views_consignee import Consignee_Request, Consignee_ID

app_name = "consignee"


urlpatterns = [
# ex: api/consignee/
path('', Consignee_Request.as_view({'get': 'get', 'post': 'post'}), name='Consignee_Request'),
# ex: api/consignee/<int:id>
path("<int:id>", Consignee_ID.as_view({'get': 'get', 'put': 'put', 'delete': 'delete'}), name='Consignee_ID')
]

