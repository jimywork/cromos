#!/usr/bin/python

import requests
import os
import sys
import re
import zipfile
import struct
import erros
import shutil
from libs.colors import Colors
from libs.build import Build

class Download :


	def __init__(self, extension) :

		self.extension = extension
		self.color = Colors()
		self.path = "output/extensions/{}".format(self.extension)
		
		if not os.path.exists(self.path):

			try:

				print("{} Downloading the extension {}".format(self.color.status("[+]"), self.extension))

				crx = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D{}%26installsource%3Dondemand%26uc".format(self.extension) # URL to extract the CRX
				request = requests.get(crx, headers={'user-agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'}, stream=True, timeout=5) # Send the Request
				status = request.raise_for_status() # Request status code

				if not os.path.exists("output/extensions/tmp"):
					os.mkdir("output/extensions/tmp")

				chunksize = 16 * 1024
				extension = "{}{}".format(self.extension, ".crx")

				pattern = r"[a-z]{32}"

				matches = re.search(pattern, self.extension)

				if matches:
						with open(os.path.join("output/extensions/tmp", self.extension), 'wb') as f:
							for chunk in request.iter_content(chunk_size=chunksize) :
								f.write(chunk)		
			except requests.exceptions.Timeout as e:
			    # Timeout
			    print("{} Timout Error, try again! problably the extension is big for the default timeout chrome webstore allow 100MB".format(color.error("[!]")))
			    sys.exit(1)
			except requests.exceptions.HTTPError as e:
				# HTTPError status code
			    print("{} Error, try again! problably the extension doesn't exists".format(self.color.error("[!]")))
			    sys.exit(1)

			try:

				with open(os.path.join("output/extensions/tmp", self.extension), 'rb') as f :

					magic = f.read(4)
					if magic != "Cr24":
						print("{} The file {} is corrupted".format(color.error("[!]"), self.extension))

					version = f.read(4)
					version, = struct.unpack("<I", version)

					public_key_length = f.read(4)
					public_key_length, = struct.unpack("<I", public_key_length)

					signature_key_length = f.read(4)
					signature_key_length, = struct.unpack("<I", signature_key_length)

					f.seek(public_key_length + signature_key_length, os.SEEK_CUR)

					outzip = "{}{}".format(self.extension, ".zip")

					with open(os.path.join("output/extensions/tmp", outzip), 'wb') as ezip :
						while 1:
							buff = f.read(1)

							if not buff:
								break
							ezip.write(buff)

					ezip.close()
			except Exception as e:
				print("{} Unpack file falid".format(self.color.error("[!]")))
				sys.exit(1)

			zipile = "output/extensions/tmp/{}{}".format(self.extension, ".zip")
			extracted = "output/extensions/%s" % (self.extension)

			try:
				with zipfile.ZipFile(zipile, "r") as extract :
					extract.extractall(extracted)
					extract.close()
			except Exception as e:
				print("{} Extract file falid{}".format(self.color.error("[!]"), self.extension))
				sys.exit(1)

			error = erros.Errors(self.extension)
			error.folders()	
			error.keys()

			if os.path.exists("output/extensions/tmp"):
				shutil.rmtree("output/extensions/tmp")

			print("{} Extension directory output/extension/{}".format(self.color.status("[+]"), self.extension))
		elif os.path.exists(self.path):
			print("{} The extension has already been downloaded".format(self.color.yellows("[!]")))