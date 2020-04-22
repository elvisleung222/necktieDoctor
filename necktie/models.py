from django.db import models

# TODO: put an ER diagram to README


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
    language = models.ManyToManyField(Language, related_name='languages')
    clinic = models.ManyToManyField(
        Clinic,
        related_name='clinics',
        through='Consultation',
        through_fields=('doctor', 'clinic')
    )
    category = models.ManyToManyField(
        Category,
        related_name='categories',
        through='Consultation',
        through_fields=('doctor', 'category')
    )


class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    price = models.IntegerField()
    medicine = models.TextField()


