from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'servers', views.ServerListViewSet, base_name='servers')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^info/(?P<user>.+)/(?P<host>.+)/(?P<port>.+)/$', views.ServerInfoView.as_view(), name='info'),
]
