from rest_framework.serializers import ModelSerializer
from monitor.models import Camera

class CameraSerializer(ModelSerializer):
    class Meta:
        model = Camera
        fields = ('name', 'url')