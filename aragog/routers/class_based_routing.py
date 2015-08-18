"""
Class Based Routing
"""
from aragog.routing.mapping import URLMap
from aragog.routing.client_error import HTTP404, HTTP405
from aragog.wsgi import get_url

from wsgiref.simple_server import make_server


class Routing(URLMap):
    """
    Class based routing composable object
    """

    def __init__(self):
        """
        Initialize Class based router with empty routes
        """
        self.mapping = dict()

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
        req_meth = environ['REQUEST_METHOD'].lower()

        routing = self.mapping.get(url, HTTP404)

        if hasattr(self, req_meth) and callable(getattr(self, req_meth)):
            return getattr(self, req_meth)(environ, start_response)
        return HTTP405(environ, start_response)
