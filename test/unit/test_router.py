"""
Tests against the Router class.
"""

import unittest
import mock

from aragog.routing.decorator import Router


class TestRouterMappings(unittest.TestCase):
    """
    Ensures router application actually gets mapped.
    """
    def simple_route(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ["hello, world!\n"]

    def test_simple_mappings(self):
        """
        Simple mappings work
        """
        router = Router()

        test_route = router.route("/")(self.simple_route)
        self.assertEqual(router.mapping, {"/": self.simple_route})
