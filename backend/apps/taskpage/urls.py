from django.urls import path, re_path

from .views import *

app_name = "taskpage"


urlpatterns = [
    # ex: api/taskpage/
    path('', Task_methods.as_view({'get': 'get', 'post': 'post'}), name='Task_methods'),
    # ex: api/taskpage/<int:id>
    path('<int:id>', Task_id.as_view({'get': 'get', 'put': 'put', 'delete': 'delete'}), name='Task_id'),
    # ex: api/taskpage/me/
    path('me/', Task_me.as_view({'get': 'get'}), name='Task_me'),
    # ex: api/taskpage/me/<str:parameter>/
    path('me/<str:parameter>/', Task_me.as_view({'get': 'get'}), name='Task_me_search'),
    # ex: api/taskpage/facilities
    path('facilities/', Facilities_request.as_view({'get': 'get'}), name='Facility_request'),
    # ex: api/taskpage/list
    path('list/', Task_Search.as_view({'get': 'list'}), name='Task_Search'),
]