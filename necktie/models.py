from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()


class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()


class District(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()


class Clinic(models.Model):
    name = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.TextField()
    service_hour = models.TextField()


class Doctor(models.Model):
    name = models.TextField()
    languages = models.ManyToManyField(Language)
    categories = models.ManyToManyField(Category)
    clinics = models.ManyToManyField(Clinic)


class Pricing(models.Model):
    # One-to-one relationship
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        primary_key=True
    )
    price = models.IntegerField()
    medicine = models.TextField()
