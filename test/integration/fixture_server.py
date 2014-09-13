"""
Tests against the URL Router
"""

from wsgiref.simple_server import make_server

from aragog import Router


router = Router()

@router.route('/')
def simple_app(environ, start_response):
    """
    Simplest possible application object
    """
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["hello, world!\n"]


@router.route('/foo')
def foo_app(environ, start_response):
    """
    Foo application. Outputs 'foobar!'
    """
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["foobar!\n"]

@router.route('/environ')
def environ_app(environ, start_response):
    """
    Outputs the full server environ passed in to the request
    """
    response_body = ['%s: %s' % (key, value)
                     for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

if __name__ == "__main__":
    httpd = make_server('', 8080, router)
    print "Server started on 8080."
    httpd.serve_forever()
