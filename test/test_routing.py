"""
Tests against the URL Router
"""

from wsgiref.simple_server import make_server

from aragog.routing.decorator import Router


router = Router()


@router.route("/")
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["hello, world!\n"]


@router.route("/foo")
def foo_app(environ, start_response):
    """Foo application. Outputs 'foobar!'"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["foobar!\n"]


if __name__ == "__main__":
    httpd = make_server('', 8080, router)
    print "Server started on 8080."
    httpd.serve_forever()
