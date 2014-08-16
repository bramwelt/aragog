"""
A Collection of WSGI Helpers
"""


def get_url(environ):
    """
    Extract the path from a URL
    """
    return urlsplit(environ['PATH_INFO']).path
