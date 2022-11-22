#!/bin/sh

cd src
python manage.py migrate
python manage.py loaddata countries.json
python manage.py loaddata cities.json
python manage.py runserver 0.0.0.0:8000

