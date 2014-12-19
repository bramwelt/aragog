"""
Shared URL Mapping
"""

class URLMap(object):
    """
    URLMap is a mapping of URLs to functions.
    """

    def add_route(self, url, func):
        """
        Adds a route to the mapping

        :param str url: URL the func should be associated with.
        :param callable func: Function URL will be associated with.
        :return: None
        """
        if url not in self.mapping:
            self.mapping[url] = func
        else:
            raise KeyError("Route already exists: {}".format(url))
