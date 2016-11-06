import json

from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.core.exceptions import ObjectDoesNotExist

from .client_script import ClientConnection
from .models import Server
from .serializers import ServerSerializer
from accounts.models import Customer


class ServerListViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ServerInfoView(views.APIView):
    lookup_fields = ('user', 'host', 'port')
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kw):
        try:
            user_inst = Customer.objects.get(pk=request.user.id)
        except ObjectDoesNotExist:
            return Response("User doesnt exist", status=status.HTTP_400_BAD_REQUEST)
        else:
            conn = ClientConnection(host=self.kwargs['host'], port=int(self.kwargs['port']))
            result = conn.get_data()
            jresult = json.loads(result)
            return Response(jresult, status=status.HTTP_200_OK)
