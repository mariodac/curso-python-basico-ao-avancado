#!/bin/sh
makemigrations.sh
echo 'Executando migrate...'
python manage.py migrate --noinput