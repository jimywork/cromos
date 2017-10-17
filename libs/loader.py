#!/usr/bin/python


class Loader :

	def __init__(self, extension, module) :

		self.module = module
		self.extension = extension
		
	def inject(self) :
		print(self.module)
