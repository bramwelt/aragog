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

        :param dict environ: The WSGI environ.
        :param callable start_response: The start_response callable for
            a WSGI application.
        :return: The WSGI application mapped to the URL in the environ.
        :rtype: callable
        """
        url = get_url(environ)
        routing, methods = self.mapping.get(url, (HTTP404, http_methods))
        if environ['REQUEST_METHOD'] not in methods:
            return HTTP405(environ, start_response)
        return routing(environ, start_response)

    def add_route(self, url, func, methods):
        """
        Adds a route to the mapping

        :param str url: Route func should be attached at.
        :param callable func: Function route will be attached to.
        :param list methods: Accepted HTTP methods.
        :return: None
        """
        if url not in self.mapping:
            self.mapping[url] = (func, methods)
        else:
            raise KeyError("Route already exists: {}".format(url))

    def route(self, uri, methods=["GET"]):
        """
        Route a request to a function

        :param string uri: URI the function can be called from.
        :param list methods: List of HTTP methods the route will accept.
        :return: A wrapped function.
        """
        m = ["HEAD"]
        m.extend(methods)
        def app_wrapper(f):
            self.add_route(uri, f, m)
            return f
        return app_wrapper
