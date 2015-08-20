Aragog
======

.. warning:: Aragog is under active development. Use at your own risk.

Aragog is a collection of python URL routers heavily influenced by
Django and Flask. It does not provide a request wrapper but maps routes
directly to WSGI callable functions.

Instead of restricting users to a single interface, Aragog provides 4
different ways of attaching routes:

 1. Decorator
 2. File
 3. MVC
 4. Class

Decorator is the default router and can be accessed with:

    from aragog import Router

All routers can be access from:

    from aragog.routing.(class|decorator|file|mvc) import Router

Decorator
---------

    from aragog import Router

    router = Router()

    @router.route('/')
    def hello_world(environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Hello, world!\n']

File
----

    # urls.py

    from aragog.routing.file import Router

    from app.views import foo, bar, baz

    router = Router()
    url = router.url

    router.urls = [
        url('/', foo),
        url('/search', bar),
        url('/edit, baz)
    ]

MVC
---
    # foo.py

    class Foo(object):
        def home(environ, start_response): pass
        def search(environ, start_response): pass


    # urls.py

    from aragog.routing.mvc import Router

    from foo import Foo

    router = Router()

    router.url('/', class=Foo, view='home')
    router.url('/search', class=Foo, view='search')

Class
-----

    # foo.py

    class Foo(object):
        def get(environ, start_response): pass
        def put(environ, start_response): pass
        def post(environ, start_response) pass


    # urls.py

    from aragog.routing.class import Router

    from foo import Foo

    router = Router()

    router.url('/foo', class=Foo)
