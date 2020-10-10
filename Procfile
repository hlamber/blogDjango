web: gunicorn blogDjango.wsgi --log-file -
heroku ps:scale web=1*
web: python myApp.py runserver 0.0.0.0:$PORT


