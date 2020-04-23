# Create your views3 here.
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from ..models import Doctor, Consultation
from .consultationView import CategorySerializer, ClinicSerializer, LanguageSerializer


class ConsultationSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Consultation
        fields = ['category', 'clinic', 'price', 'medicine']


class DoctorSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(
        many=True,
        read_only=True,
    )
    consultation_services = ConsultationSerializer(
        many=True,
        read_only=True,
        source='consultation_set'
    )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'language', 'consultation_services']


class DoctorRetrieveAPIView(RetrieveAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_field = 'id'
