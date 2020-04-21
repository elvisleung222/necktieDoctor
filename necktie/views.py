from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, BaseRangeFilter, NumberFilter
from rest_framework.generics import ListAPIView
from .models import Language, Category, District, Clinic, Doctor, Consultation
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
        read_only=True,
    )

    class Meta:
        model = Clinic
        fields = ['name', 'district', 'address', 'phone_number', 'service_hour']


class DoctorSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'language']


class ConsultationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Consultation
        fields = ['doctor', 'category', 'clinic', 'price', 'medicine']


class NumberRangeFilter(BaseRangeFilter, NumberFilter):
    pass


class ConsultationFilter(FilterSet):
    category = CharFilter('category__code')
    district = CharFilter('clinic__district__code')
    language = CharFilter('doctor__language__code')
    price_range = NumberRangeFilter(field_name='price', lookup_expr='range')

    class Meta:
        model = Consultation
        fields = ['category', 'district', 'language', 'price_range']


class ConsultationListAPIView(ListAPIView):
    """
    API view to retrieve list of doctor
    """
    serializer_class = ConsultationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultationFilter
    queryset = Consultation.objects.all()

# TODO: clean up all names of serializer and remove unneeded stuffs
class Consultation_2_Serializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Consultation
        fields = ['category', 'clinic', 'price', 'medicine']


class Doctor_2_Serializer(serializers.ModelSerializer):
    language = LanguageSerializer(
        many=True,
        read_only=True,
    )
    consultation_services = Consultation_2_Serializer(
        many=True,
        read_only=True,
        source='consultation_set'
    )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'language', 'consultation_services']

# TODO: use View to replace the below query
def query_doctor(request, key):
    queryset = Doctor.objects.get(id=key)
    serializer = Doctor_2_Serializer(queryset, many=False)
    return JsonResponse(serializer.data)
