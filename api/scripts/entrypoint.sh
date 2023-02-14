#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0

# TODO: Only for local entrypoint.sh
DJANGO_SUPERUSER_PASSWORD="1" python manage.py createsuperuser --noinput --username admin

exec "$@"

python manage.py runserver 0.0.0.0:8000
