
from django.contrib import admin
from django.urls import path
from necktie.views.consultationView import ConsultationListAPIView
from necktie.views.doctorView import DoctorRetrieveAPIView

urlpatterns = [
    path('admin/', admin.site.urls), # TODO: see if remove this path
    path('doctor/', ConsultationListAPIView.as_view()),
    path('doctor/<int:id>', DoctorRetrieveAPIView.as_view()),
]

