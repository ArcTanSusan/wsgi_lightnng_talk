from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

import hello_pyramid
import hello_flask

application = DispatcherMiddleware(hello_pyramid.app, {
    '/combined':     hello_flask.app
})


if __name__ == '__main__':
    run_simple('localhost', 9000, application,
        use_reloader=True, use_debugger=True, use_evalex=True)
