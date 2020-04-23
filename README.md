# Necktie Doctor Django Application

## Entity Relationship Diagram
![ER Diagram](ER_diagram.png)

## Get Started

### 1. Create sqlite database
```shell script
python manage.py migrate
```

### 2. Run tests
```shell script
python manage.py test
```

### 3. Run application
```shell script
python manage.py runserver
```

### 4. Test APIs

- List all doctors
  
  http://127.0.0.1:8000/doctor/

- Search a doctor by ID
  
  http://127.0.0.1:8000/doctor/< id >

## Utils

### Generate ER Diagram
```shell script
python manage.py graph_models -a > erd.dot
dot -Tpng erd.dot -o erd.png
```

### Generate requirements.txt
```shell script
pip freeze > requirements.txt
```
