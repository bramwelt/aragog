"""
Integration Tests for Decorator Routing
"""

from aragog.routing.decorator import Router

from webtest import TestApp

import unittest


router = Router()

@router.route('/foo')
def home(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, world!']


class TestDecorator(unittest.TestCase):
    """
    Ensure the decorators are applied and route correctly
    """

    def setUp(self):
        """
        Start each test with a new Router instance
        """
        self.app = TestApp(router)

    def test_root_route(self):
        """
        WebTest a basic route
        """
        resp = self.app.get('/foo')

        self.assertEqual(resp.status_int, 200)
        self.assertEqual(resp.content_type, 'text/plain')
        self.assertIn('wor', resp)
        self.assertEqual(1, len(router.mapping))

    def test_route_not_found(self):
        """
        WebTest to make sure a route doesn't show up
        """
        resp = self.app.get('/bar', status=404)

        self.assertEqual(resp.status_int, 404)

    def test_method_not_allowed(self):
        """
        WebTest to check that method is not accepted
        """
        for method in ['HEAD', 'GET']:
            resp = self.app.request('/foo', method=method)
            self.assertEqual(resp.status_int, 200)
        
        for method in ['POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS',
                       'TRACE']:
            resp = self.app.request('/foo', method=method, status=405)
            self.assertEqual(resp.status_int, 405)

    @unittest.skip("WebTest does not support HTTP 501 NOT IMPLEMENTED yet")
    def test_not_implemented(self):
        """
        WebTest to check response returns 'NOT IMPLEMENTED' on
        unrecognized methods
        """
        resp = self.app.request('/foo', method='HERPS', status=501)
        self.assertEqual(resp.status_int, 501)
