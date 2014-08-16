"""
Client Error HTTP Status Callables
"""


def HTTP404(environ, start_response):
    """
    HTTP 404 Response
    """
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['']
