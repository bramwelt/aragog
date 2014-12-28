.. _decorator-based:

Decorator Routing
=================

Those familiar with the Flask micro-framework will see many similarities
between both `URL routers`_. The major difference here is that Aragog
routes to a WSGI application: something Flask developers would not like
you to worry about, for good reason.

Decorator based routers provide users the path of least resistance for
constructing a URL. The router works by adding a ``@router.route``
decorator to a function, passing in the name of the route.

.. Note:: Aragog does not provide you with a global URL router: one
          which you could simply use ``@route`` without a router
          instance. This is for your `own good`_.

Here is an example of how to use the decorator router::

    from wsgiref.simple_server import make_server

    from aragog import Router
    router = Router()

    @router.route('/')
    def hello_world(environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Hello, world!\n']

    if __name__ == '__main__':
        httpd = make_server('', 8080, router)
        httpd.serve_forever()


This will register a single route ``/`` that will run the function
``hello_world``, which returns an HTTP *text/plain* response of **Hello,
world!**.


.. _URL routers: http://flask.pocoo.org/docs/0.10/api/#url-route-registrations
.. _own good: http://stackoverflow.com/questions/19158339/python-why-are-global-variables-evil
