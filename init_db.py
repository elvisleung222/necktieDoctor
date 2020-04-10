import os
from necktie.models import Language, Category, District, Clinic, Doctor, Pricing

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
d1.languages.add(l1, l2)
d1.clinics.add(clin1)
d1.save()


d2 = Doctor(name='Law Siu Tong')
d2.save()
d2.languages.add(l2)
d2.clinics.add(clin2)
d2.save()


# d3 = Doctor(name='鄭小強')
# d3.languages.add(l2, l3)
# d3.save()
#
# d4 = Doctor(name='李小明')
# d4.languages.add(l2)
# d4.save()
#
# d5 = Doctor(name='鄭小強')
# d5.languages.add(l2, l3)
# d5.save()


