
import os
from libs.colors import Colors

class Build :

	global color

	color = Colors()

	def __init__(self, extension, filetype) :
		self.extension = extension
		self.filetype = filetype

	def builder(self) :
		
		try:

			path = "output/builds/" # Builds files

			if self.filetype == "bat":
				payloads = "data/payloads/powershell/powershell.txt" # Payload file
			elif self.filetype == "vbs" :
				payloads = "data/payloads/VBScript/vbs.txt" # Payload file

			print(color.status("[+] Execuable file in directory output/extension/{}".format(self.extension)))
		
			build = "{}.{}".format(self.extension, self.filetype) # Make .bat file

			with open(payloads, 'r') as f :

				# Set the drop URL or do not
				payload = f.read()

				payload = payload.replace('***', 'a')

				with open(os.path.join(path, build), 'w') as builder :
					# Write the new file
					builder.write(payload)
		except IOError as e:
			raise e

