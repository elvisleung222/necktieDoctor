from django.test import TestCase
from .views import ConsultationSerializer, LanguageSerializer, CategorySerializer, DistrictSerializer, ClinicSerializer, \
    DoctorSerializer
from .models import Language, Category, District, Clinic, Doctor, Consultation
import json
from django.test import Client

client = Client()


class ConsultationTest(TestCase):

    def setUp(self):
        l1 = Language(code='en', name='English')
        l2 = Language(code='zh-hk', name='Cantonese')
        l3 = Language(code='zh-cn', name='Mandarin')
        l1.save()
        l2.save()
        l3.save()

        dist1 = District(code='yuen-long', name='Yuen Long')
        dist2 = District(code='tuen-mun', name='Tuen Mun')
        dist3 = District(code='tsuen-wan', name='Tsuen Wan')
        dist4 = District(code='tai-po', name='Tai Po')
        dist5 = District(code='sha-tin', name='Sha Tin')
        dist6 = District(code='kwun-tong', name='Kwun Tong')
        dist1.save()
        dist2.save()
        dist3.save()
        dist4.save()
        dist5.save()
        dist6.save()

        cat1 = Category(code='dental', name='Dental')
        cat2 = Category(code='chinese-med', name='Chinese Medicine')
        cat3 = Category(code='general', name='General')
        cat4 = Category(code='acupuncture', name='Acupuncture')
        cat5 = Category(code='x-ray', name='X-Ray')
        cat6 = Category(code='physio', name='Physiotherapy')
        cat1.save()
        cat2.save()
        cat3.save()
        cat4.save()
        cat5.save()
        cat6.save()

        clin1 = Clinic(name='Tencent Doctorwork', address='Shop B82 1/F Tsuen Fung Centre Tsuen Wan NT',
                       phone_number='2156 5893', service_hour='Monday')
        clin1.district = dist2
        clin1.save()

        clin2 = Clinic(name='AI Medical',
                       address='Room 40, Ground Floor, Jade Field Garden, 15-19 Ngau Tau Kok Road, Ngau Tau Kok, Kowloon',
                       phone_number='2156 5893', service_hour='Monday')
        clin2.district = dist3
        clin2.save()

        d1 = Doctor(name='Law Siu Tong')
        d1.save()
        d1.language.add(l1, l2)
        cc1 = Consultation(doctor=d1, category=cat2, clinic=clin1, price=120, medicine='3 days')
        cc1.save()
        cc2 = Consultation(doctor=d1, category=cat4, clinic=clin2, price=180, medicine='2 days')
        cc2.save()
        d1.save()

        d2 = Doctor(name='Cheng Ka keung')
        d2.save()
        d2.language.add(l2)
        cc3 = Consultation(doctor=d2, category=cat2, clinic=clin1, price=120, medicine='3 days')
        cc3.save()
        cc4 = Consultation(doctor=d2, category=cat4, clinic=clin2, price=180, medicine='2 days')
        cc4.save()
        cc5 = Consultation(doctor=d2, category=cat5, clinic=clin2, price=140, medicine='5 days')
        cc5.save()
        d2.save()

    # Serializers
    def test_language_serializer(self):
        expected = {
            'code': 'en',
            'name': 'English'
        }

        language = Language.objects.get(code='en')
        serializer = LanguageSerializer(language)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    def test_category_serializer(self):
        expected = {
            'code': 'chinese-med',
            'name': 'Chinese Medicine'
        }

        category = Category.objects.get(code='chinese-med')
        serializer = CategorySerializer(category)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    def test_district_serializer(self):
        expected = {
            'code': 'tsuen-wan',
            'name': 'Tsuen Wan'
        }

        district = District.objects.get(code='tsuen-wan')
        serializer = DistrictSerializer(district)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    def test_clinic_serializer(self):
        expected = {
            "name": "AI Medical",
            "district": {
                "code": "tsuen-wan",
                "name": "Tsuen Wan"
            },
            "address": "Room 40, Ground Floor, Jade Field Garden, 15-19 Ngau Tau Kok Road, Ngau Tau Kok, Kowloon",
            "phone_number": "2156 5893",
            "service_hour": "Monday"
        }

        clinic = Clinic.objects.get(name='AI Medical')
        serializer = ClinicSerializer(clinic)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    def test_doctor_serializer(self):
        expected = {
            "id": 1,
            "name": "Law Siu Tong",
            "language": [
                {
                    "code": "en",
                    "name": "English"
                },
                {
                    "code": "zh-hk",
                    "name": "Cantonese"
                }
            ]
        }

        doctor = Doctor.objects.get(id=1)
        serializer = DoctorSerializer(doctor)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    def test_consultation_serializer(self):
        expected = {
            "doctor": {
                "id": 2,
                "name": "Cheng Ka keung",
                "language": [
                    {
                        "code": "zh-hk",
                        "name": "Cantonese"
                    }
                ]
            },
            "category": {
                "code": "x-ray",
                "name": "X-Ray"
            },
            "clinic": {
                "name": "AI Medical",
                "district": {
                    "code": "tsuen-wan",
                    "name": "Tsuen Wan"
                },
                "address": "Room 40, Ground Floor, Jade Field Garden, 15-19 Ngau Tau Kok Road, Ngau Tau Kok, Kowloon",
                "phone_number": "2156 5893",
                "service_hour": "Monday"
            },
            "price": 140,
            "medicine": "5 days"
        }

        consultation = Consultation.objects.get(price=140)
        serializer = ConsultationSerializer(consultation)
        self.assertEqual(expected, json.loads(json.dumps(serializer.data)))

    # Views and APIs
    def test_all_consultation(self):
        res = client.get('/doctor/')
        res = json.loads(res.content)
        self.assertEqual(5, len(res))

    def test_get_doctor_by_id(self):
        expected_id = 2
        res = client.get('/doctor/' + str(expected_id))
        res = json.loads(res.content)
        self.assertEqual(expected_id, res['id'])

    def test_consultation_filter_district(self):
        expected_districts = ['tuen-mun', 'tsuen-wan']
        for expected_district in expected_districts:
            res = client.get('/doctor/', {'district': expected_district})
            res = json.loads(res.content)
            for con in res:
                self.assertEqual(expected_district, con['clinic']['district']['code'])

    def test_consultation_filter_district_price(self):
        expected_district = 'tsuen-wan'
        expected_price_min = 130
        expected_price_max = 150

        res = client.get('/doctor/', {'district': expected_district,
                                      'price_range': str(expected_price_min) + ',' + str(expected_price_max)})
        res = json.loads(res.content)
        for con in res:
            self.assertEqual(expected_district, con['clinic']['district']['code'])
            self.assertTrue(expected_price_min <= con['price'] <= expected_price_max)

    def test_consultation_filter_language(self):
        expected_language = 'zh-hk'
        res = client.get('/doctor/', {'language': expected_language})
        res = json.loads(res.content)
        for con in res:
            check = False
            languages = con['doctor']['language']
            for lang in languages:
                if lang['code'] == expected_language:
                    check = True
            # language array must contain the expected language
            self.assertTrue(check)

    def test_consultation_filter_category(self):
        expected_category = 'x-ray'
        res = client.get('/doctor/', {'category': expected_category})
        res = json.loads(res.content)
        for con in res:
            self.assertEqual(expected_category, con['category']['code'])
