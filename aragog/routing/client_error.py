"""
Client Error HTTP Status Callables
"""


class HTTP404(object):
    """
    HTTP 404 Response
    """

    def __call__(self, environ, start_response):
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return ['']
