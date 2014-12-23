.. _decorator-based:

Decorator Routing
=================

A decorator based router give users the greatest freedom to what
function is routed to. This works by adding a ``@route`` decorator to
each function, along with the name of the route.

Here is an example of how to use the decorator router::

    from wsgiref.simple_server import make_server

    from aragog import Router
    router = Router()


    @router.route('/')
    def hello_world(environ, start_response):
        """
        Simplest possible application object
        """
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ['hello, world!\n']


    if __name__ == '__main__':
        httpd = make_server('', 8080, router)
        httpd.serve_forever()


This will register a single route ``/`` that will run the function
``hello_world``.

This is similar to the Flask way of `URL routing`_.

.. _URL routing: http://flask.pocoo.org/docs/0.10/api/#url-route-registrations
