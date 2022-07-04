# Django-JWTAuth-Redis-REST API





## Installation
git clone https://github.com/silpathomas/django_rest_framework_map.git

1.Create a virtual environment using following command

    python -m venv map-env

2.Activate  virtual environment

    source map-env/bin/activate

3.iInstall the requirements

    pip install -r requirement.txt

4.Change the database details in settings.py file

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'map', 
        'USER': 'postgres', 
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

5.Apply Migrations

       python manage.py migrate
6.Create Superuser  using following command

	python manage.py createsuperuser
7.Run the project using below commad

	Python manage.py runserver
  
8.Create User and Geolocations using admin panel

	http://localhost:8000/admin/


### API

POST api/account/token/  for Login

GET  api/geolocation/list for listing location
