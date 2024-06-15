#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

# uWSGI: 유저가 보낸 데이터를 Nginx가 데이터를 받아오고, Django랑 소통을 하는 역활
uwsgi --socket :9000 --module config.wsgi --master --enable-threads --workers 4
