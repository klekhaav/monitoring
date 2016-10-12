from datetime import date

from rest_framework import serializers

from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'user_email', 'title', 'address', 'protocol')
        read_only_fields = ('id',)