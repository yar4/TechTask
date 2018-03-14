from django.shortcuts import get_object_or_404
from rest_framework import generics
from apps.OTC.api.serializers import OTCSerializer
from apps.OTC.models import OTCRegistration

class CreateOTC(generics.CreateAPIView):
    queryset = OTCRegistration.objects.all()
    serializer_class = OTCSerializer

