"""
A Collection of WSGI Helpers
"""
from urlparse import urlsplit


http_methods = frozenset(["CONNECT",
                         "DELETE",
                         "GET",
                         "HEAD",
                         "OPTIONS",
                         "PATCH",
                         "POST",
                         "PUT",
                         "TRACE"])

def get_url(environ):
    """
    Extract the path from a URL
    """
    return urlsplit(environ['PATH_INFO']).path
