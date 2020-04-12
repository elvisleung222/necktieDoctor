from django.shortcuts import render


# Create your views here.
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Doctor, Language, Category, District, Clinic, Doctor, ConsultationCategory
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


class ConsultationCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = ConsultationCategory
        fields = ['category', 'price', 'medicine']


class DoctorSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(
        many=True,
        read_only=True,
    )
    clinic = ClinicSerializer(
        many=True,
        read_only=True,
    )
    consultation_details = ConsultationCategorySerializer(
        many=True,
        read_only=True,
        source='consultationcategory_set'
    )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'language', 'clinic', 'consultation_details']


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

