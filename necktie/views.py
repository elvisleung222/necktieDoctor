from django.shortcuts import render


# Create your views here.
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Doctor, Language, Category, District, Clinic, Doctor, Pricing
from django.http import JsonResponse


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['code', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['code', 'name']


class ClinicSerializer(serializers.ModelSerializer):
    district = LanguageSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = Clinic
        fields = ['name', 'district', 'address', 'phone_number', 'service_hour']

class DoctorSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(
        many=True,
        read_only=True,
    )
    categories = CategorySerializer(
        many=True,
        read_only=True,
    )
    clinics = ClinicSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'languages', 'categories', 'clinics']

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

