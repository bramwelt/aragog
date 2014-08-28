"""
Test against the Router class
"""
import unittest
import apitestcase

class TestBasicRoutes(unittest.TestCase, apitestcase.TestCase):
    """
    Integration test on GET methods
    """
    def test_root(self):
        self.assertGet("http://localhost:8080/", contains=["hello, world!"])

    def test_foo(self):
        self.assertGet("http://localhost:8080/foo", contains=["foobar!"])

if __name__ == "__main__":
    unittest.main()
