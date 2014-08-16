#! /usr/bin/env python
"""
Aragog Router Decorator
-----------------------

Convert any function into a WSGI endpoint with a simple decorator.
"""

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
