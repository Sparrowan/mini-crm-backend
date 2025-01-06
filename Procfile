web: gunicorn minicrm.wsgi --log-file - 
#or works good with external database
web: celery -A minicrm worker -l info & celery -A minicrm beat -l info & python manage.py migrate && gunicorn minicrm.wsgi