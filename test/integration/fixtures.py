"""
Integration Test Fixtures
"""

from wsgiref.simple_server import make_server

from aragog.routers.decorator import Router


router = Router()
environ_router = Router()

@router.route('/foo')
def foo(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, world!']


@environ_router.route('/')
def environ_app(environ, start_response):
    """
    Outputs the full server environ passed in to the request.

      Wsgiref populates environ with a few extra things thay may
      normally/actually be there.
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
    httpd = make_server('', 8080, environ_router)
    print "Server started on 8080."
    httpd.serve_forever()
