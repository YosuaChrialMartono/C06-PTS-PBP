release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata initial_faq_data.json'
web: python manage.py migrate && gunicorn project_django.wsgi && python manage.py loaddata initial_faq_data.json
