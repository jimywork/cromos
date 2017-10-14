#!/usr/bin/python


class Loader :

	def __init__(self, module) :

		self.module = module
		
	def inject(self) :
		print(self.module)
