#!/usr/bin/python

import webapp
import random


class adiosApp(webapp.webApp):

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><strong>Good bye World!!!!!</strong></body></html>")

if __name__ == "__main__":
	adios = adiosApp("localhost", 1234)
