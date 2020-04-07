# necktieDoctor


## Get Started

### 1. Create sqlite database
```sh
python manage.py migrate
```

### 2. Run application
```sh
python manage.py runserver
```

### 3. Test APIs

- List all doctors
  
  http://127.0.0.1:8000/doctor/

- Search a doctor by ID
  
  http://127.0.0.1:8000/doctor/<id\>
