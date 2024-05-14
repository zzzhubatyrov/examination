from django.urls import path, re_path

from ..views.views_kpp import KPP_Request, KPP_ID, KPP_Search, KPP_Me, Equipment_Template_Request

app_name = "kpp"

urlpatterns = [
    # ex: api/kpp/
    path('', KPP_Request.as_view({'get': 'get', 'post': 'post'}), name='kpp'),
    # ex" api/kpp/<int:id>
    path('<int:id>', KPP_ID.as_view({'get': 'get', 'put': 'put'}), name='kpp_id'),
    # ex: api/kpp/search/
    path('search/', KPP_Search.as_view({'get': 'list'}), name='KPP_Search'),
    # ex: api/kpp/me/
    path('me/', KPP_Me.as_view({'get': 'get'}), name='KPP_Me'),
    # ex: api/kpp/equipment_template
    path('equipment_template/', Equipment_Template_Request.as_view({'get': 'get'}), name='Equipment_Template_Request'),
]