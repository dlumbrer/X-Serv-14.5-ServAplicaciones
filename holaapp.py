#!/usr/bin/python

import webapp
import random


class holaApp(webapp.webApp):

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><strong>Hello World!!!!!</strong></body></html>")

if __name__ == "__main__":
	hola = holaApp("localhost", 1234)
