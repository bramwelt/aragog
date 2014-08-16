#! /usr/bin/env python
"""
Aragog Router Decorator
-----------------------

Convert any function into a WSGI endpoint with a simple decorator.
"""

from wsgiref.simple_server import make_server
from urlparse import urlsplit

from aragog.wsgi import get_url
from aragog.routing.client_error import HTTP404


class Router(object):
    """
    Router holds the mapping of routes to callables.
    """

    def __init__(self):
        """
        Instance level route mapping
        """
        self.mapping = {}

    def __call__(self, environ, start_response):
        """
        Get a WSGI request, and pass it on to the correct callable.
        """
        routing = self.mapping.get(get_url(environ), HTTP404())
        return routing(environ, start_response)

    def add_route(self, url, func):
        """
        Adds a route to the mapping
        """
        if url not in self.mapping:
            self.mapping[url] = func
        else:
            raise KeyError("Route already exists: {}".format(url))

    def route(self, uri):
        """
        Route a request to a function

        :param: uri
        :param_type: string
        """
        def app_wrapper(f):
            self.add_route(uri, f)
            return f
        return app_wrapper

router = Router()

@router.route("/")
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["hello, world!\n"]


@router.route("/foo")
def foo_app(environ, start_response):
    """Foo application. Outputs 'foobar!'"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["foobar!\n"]


if __name__ == "__main__":
    httpd = make_server('', 8080, router)
    print "Server started on 8080."
    httpd.serve_forever()
