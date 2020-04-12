from necktie.models import Language, Category, District, Clinic, Doctor, ConsultationCategory

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


clin1 = Clinic(name='Tencent Doctorwork', address='Shop B82 1/F Tsuen Fung Centre Tsuen Wan NT', phone_number='2156 5893', service_hour='Monday')
clin1.district = dist2
clin1.save()

clin2 = Clinic(name='AI Medical', address='Room 40, Ground Floor, Jade Field Garden, 15-19 Ngau Tau Kok Road, Ngau Tau Kok, Kowloon', phone_number='2156 5893', service_hour='Monday')
clin2.district = dist3
clin2.save()


d1 = Doctor(name='Law Siu Tong')
d1.save()
d1.language.add(l1, l2)
d1.clinic.add(clin1)
cc1 = ConsultationCategory(doctor=d1, category=cat2, price=120, medicine='3 days')
cc1.save()
cc2 = ConsultationCategory(doctor=d1, category=cat4, price=180, medicine='2 days')
cc2.save()
d1.save()


d2 = Doctor(name='Cheng Ka keung')
d2.save()
d2.language.add(l2)
d2.clinic.add(clin2)
cc3 = ConsultationCategory(doctor=d2, category=cat2, price=120, medicine='3 days')
cc3.save()
cc4 = ConsultationCategory(doctor=d2, category=cat4, price=180, medicine='2 days')
cc4.save()
cc5 = ConsultationCategory(doctor=d2, category=cat5, price=140, medicine='5 days')
cc5.save()
d2.save()
