from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClassificationSerializer
from .serializer import ImpactSerializer
from .serializer import OrbitSerializer
from .models import Classification
from .models import Impacts
from .models import Orbits
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.views import APIView

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]

class ImpactViewSet(viewsets.ModelViewSet):
    queryset = Impacts.objects.all()
    serializer_class = ImpactSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]

class OrbitViewSet(viewsets.ModelViewSet):
    queryset = Orbits.objects.all()
    serializer_class = OrbitSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]