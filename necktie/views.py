from django.shortcuts import render


# Create your views here.
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Doctor
from django.http import JsonResponse


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name']


class DoctorListAPIView(ListCreateAPIView):
    """
    API view to retrieve list of doctor
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


def query_doctor(request, key):
    queryset = Doctor.objects.get(id=key)
    serializer = DoctorSerializer(queryset, many=False)
    return JsonResponse(serializer.data)

