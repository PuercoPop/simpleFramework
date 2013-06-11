#!/usr/bin/env python

class Request(object):
        def __init__(self, method="GET", version="HTTP/1.1",
                     route='/', headers=None, get_vars=None, body=None):

                if headers is None:
                        headers = {}
                if get_vars is None:
                        get_vars = {}

                self.method = method
		self.headers = headers
		self.route = route
		self.body = body
		self.version = version
