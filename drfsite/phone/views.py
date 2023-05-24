from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from .serializers import PhoneSerializer
from .models import Phone, Category


class PhoneAPIList(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PhoneAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PhoneAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = (IsAdminReadOnly,)
