import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        model = Phone
        fields = "__all__"

