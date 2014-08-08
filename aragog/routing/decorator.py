#! /usr/bin/env python
"""
Aragog Router Decorator
-----------------------

Convert any function into a WSGI endpoint with a simple decorator.
"""

from wsgiref.simple_server import make_server

#def debug_env(env):
#    for k, v in env.iteritems():
#        yield "{0}: {1}\n".format(k, v)

def route(uri):
    """
    Route a request to a function

    :param: uri
    :param_type: string
    """

    def app_wrapper(f):
        def app(environ, start_response):
            for k,v in environ.iteritems():
                print " + {0}: {1}".format(k, v)
            return f(environ, start_response)
        return app
    return app_wrapper

@route("/")
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ["hello, world!\n"]

if __name__ == "__main__":
    httpd = make_server('', 8080, simple_app)
    print "Server started on 8080."
    httpd.serve_forever()
