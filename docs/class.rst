.. _class-based:

Class Routing
=============

The class based URL router is a combination of file based routing and a
Routing composition class.

When a class extends the Routing composition class, and that class is
routed to, all HTTP requests are routed to the repective methods defined
on the class. For example, given a class Foo that is mapped to the URL
'/foo', an HTTP GET request to '/foo' would result in a call to `Foo.get`.

This routing is defined for each HTTP request method, excluding
`CONNECT`.

This is similar to the Rails way of URL routing.

In a file called `urls.py`::

  from aragog.routing import ClassRouter

  from myapp.endpoints import IndexUrlEndpoint


  router = ClassRouter()

  router.r('/foo', class=IndexUrlEnpoint)
