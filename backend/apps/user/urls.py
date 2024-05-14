from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

app_name = "user"

urlpatterns = [
    # ex: api/user/register/
    path("register/", RegisterView.as_view(), name="Register"),
    # ex: api/user/users/
    path("users/", Get_Users.as_view(), name="Get_Users"),
    # ex: api/user/users/search
    path("users/<str:search>/", Get_Users.as_view(), name="Get_Users"),
    # ex: api/user/me
    path("me", Get_Me.as_view({'get': 'get', 'put': 'put'}), name="Get_Me"),
    # ex: api/user/departments
    path("departments/", Department_Request.as_view({'get': 'get'}), name="Departments_Request"),
    # ex: api/user/posts
    # path("posts/", Posts_Request.as_view({'get': 'get'}), name="Posts_request"),
    # ex: api/user/login
    path('login/', login_view.as_view(), name='login'),
    # ex: api/user/logout
    path('logout', LogoutView.as_view(next_page='/'), name='logout')
]
