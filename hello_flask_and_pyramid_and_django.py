from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import hello_pyramid
import hello_flask
from hello_django.mysite.myapp import wsgi as hello_django

application = DispatcherMiddleware(hello_pyramid.app, {
    '/flask':     hello_flask.app,
    '/django':  hello_django.application
})


if __name__ == '__main__':
    run_simple('localhost', 4000, application,
        use_reloader=True, use_debugger=True, use_evalex=True)
