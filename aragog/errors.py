"""
Client Error HTTP Status Callables
"""


def HTTP404(environ, start_response):
    """
    HTTP 404 Response
    """
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['']


def HTTP405(environ, start_response):
    """
    HTTP 405 Response
    """
    start_response('405 METHOD NOT ALLOWED', [('Content-Type', 'text/plain')])
    return ['']
