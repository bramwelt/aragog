.. _decorator-based:

Decorator Routing
=================

A decorator based router give users the greatest freedom to what
function is routed to. This works by adding a ``@route`` decorator to
each function, along with the name of the route.

For example::

    @route('blog')
    def index():
        return "Welcome to my blog!"

This will register a single route ``/blog`` that will run the function
``index``.

This is similar to the Flask way of URL routing.
