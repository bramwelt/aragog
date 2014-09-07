#! /usr/bin/env python
"""
Aragog Router Decorator
-----------------------

Convert any function into a WSGI endpoint with a simple decorator.
"""

from aragog.wsgi import get_url, http_methods
from aragog.routing.client_error import HTTP404, HTTP405


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
        url = get_url(environ)
        routing, methods = self.mapping.get(url, (HTTP404, http_methods))
        if environ['REQUEST_METHOD'] not in methods:
            return HTTP405(environ, start_response)
        return routing(environ, start_response)

    def add_route(self, url, func, methods):
        """
        Adds a route to the mapping
        """
        if url not in self.mapping:
            self.mapping[url] = (func, methods)
        else:
            raise KeyError("Route already exists: {}".format(url))

    def route(self, uri, methods=["GET"]):
        """
        Route a request to a function

        :param: uri
        :param_type: string
        :param: methods
        :param_type: list of strings
        """
        m = ["HEAD"]
        m.extend(methods)
        def app_wrapper(f):
            self.add_route(uri, f, m)
            return f
        return app_wrapper
