from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Camera
from .serializer import CameraSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from monitor.models import Camera
from monitor.serializer import CameraSerializer
from rest_framework import generics
from django.http import JsonResponse,HttpResponse


# Create your views here.
class CameraList(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    def delete(self, request, pk):
        try:
            book = Camera.objects.get(pk=pk)
        except Camera.DoesNotExist:
            return HttpResponse(status=404)
        book.delete()
        return HttpResponse(status=204)