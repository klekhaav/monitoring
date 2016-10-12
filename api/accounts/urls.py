from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserListViewSet, base_name='users')

urlpatterns = [
    url(r'^', include(router.urls)),
]
