hello-django, hello-pyramid, hello-flask
===================================

This is demo Python 3.5+ code on how to run 3 different Python-based web frameworks on the same domain and port using the WSGI dispatcher.

## Running "Hello World"  using the WSGI dispatcher

    python hello_flask_and_pyramid_and_django.py

Then go to localhost:9000.

## Runnning "Hello World" with the Django web framework.

The minimum "hello world" for Django 1.4. Views only, no code having anything
to do with model/database/etc.

Assumes Django 1.4+ is installed (`pip install django` or `easy_install django`).
See "Notes" section below.

    python manage.py runserver

Then go to http://127.0.0.1:8000/.

## Runnning "Hello World" with the Pyramid web framework.

    python hello_pyramid.py

Then go to http://127.0.0.1:8000/.

## Running "Hello World"with the Flask web framework.

    python hello_flask.py

Then go to http://127.0.0.1:8000/.
