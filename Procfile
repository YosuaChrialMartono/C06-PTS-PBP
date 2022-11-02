release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py migrate --run-syncdb '
web: gunicorn project_django.wsgi --log-file -
