#!/usr/bin/python

import requests
import os
import sys
import re
import zipfile
import struct
import erros
import shutil

class CRX :

	def __init__(self, extension) :

		self.extension = extension
		
		

	def Download(self, extension) :

		try:

			crx = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D{}%26installsource%3Dondemand%26uc".format(extension) # URL to extract the CRX
			request = requests.get(crx, headers={'user-agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'}, stream=True, timeout=5) # Send the Request
			status = request.raise_for_status() # Request status code

			if not os.path.exists("output/extensions/tmp"):
				os.mkdir("output/extensions/tmp")

			chunksize = 16 * 1024
			extension = "{}{}".format(extension, ".crx")

			with open(os.path.join("output/extensions/tmp", extension), 'wb') as f:
				for chunk in request.iter_content(chunk_size=chunksize) :
					f.write(chunk)
			print("Download completed!".format(extension))		
		except requests.exceptions.Timeout as e:
		    # Timeout
		    print("{} Timout Error, try again! problably the extension is big for the default timeout chrome webstore allow 100MB".format(request.status_code))
		except requests.exceptions.HTTPError as e:
			# HTTPError status code
		    print("{} Error, try again! problably the extension doesn't exists".format(request.status_code))
		    sys.exit(1)

	def Unpack(self, extension)	 :

		try:

			crxextension = "{}{}".format(extension, ".crx")
	

			with open(os.path.join("output/extensions/tmp", crxextension), 'rb') as f :

				magic = f.read(4)
				if magic != "Cr24":
					print("The file {} is corrupted".format(extension))

				version = f.read(4)
				version, = struct.unpack("<I", version)

				public_key_length = f.read(4)
				public_key_length, = struct.unpack("<I", public_key_length)

				signature_key_length = f.read(4)
				signature_key_length, = struct.unpack("<I", signature_key_length)

				f.seek(public_key_length + signature_key_length, os.SEEK_CUR)

				outzip = "{}{}".format(extension, ".zip")

				with open(os.path.join("output/extensions/tmp", outzip), 'wb') as ezip :
					while 1:
						buff = f.read(1)

						if not buff:
							break
						ezip.write(buff)
				ezip.close()
				print("Unpack completed!".format(extension))
		except Exception as e:
			raise e

	def Extract(self, extension) :


		zipile = "output/extensions/tmp/{}{}".format(extension, ".zip")
		extracted = "output/extensions/%s" % (extension)

		# Extraindo o arquivo .crx 
		
		with zipfile.ZipFile(zipile, "r") as extract :
			extract.extractall(extracted)
			extract.close()

		# Tratando alguns erros

		error = erros.Errors(extension)
		error.removeFolders(extension)	
		error.removeKeys(extension)

		shutil.rmtree("output/extensions/tmp")
		
		print("Extract completed!".format(extension))


	def Valid(self, extension) :

		pattern = r"[a-z]{32}"

		matches = re.search(pattern, extension)

		if matches:
			return True