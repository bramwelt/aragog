"""
A Collection of WSGI Helpers
"""
from urlparse import urlsplit


def get_url(environ):
    """
    Extract the path from a URL
    """
    return urlsplit(environ['PATH_INFO']).path
