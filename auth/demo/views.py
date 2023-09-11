from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from demo.serializers import AdvSerializer
from demo.models import Adv


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
