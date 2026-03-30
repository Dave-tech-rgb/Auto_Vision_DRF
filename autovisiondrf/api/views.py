from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Device, DetectionLog
from .serializers import DeviceSerializer, DetectionLogSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetectionLogViewSet(viewsets.ModelViewSet):
    queryset = DetectionLog.objects.all().order_by('-date', '-time')
    serializer_class = DetectionLogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
