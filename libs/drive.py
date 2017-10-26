#!/usr/bin/python


"""Upload the contents of your Downloads folder to Dropbox.
This is an example app for API v2.
"""

import os
import dropbox
import zipfile
import datetime
import time

class Drive :

	def __init__(self, extension, token) :
		self.extension = extension
		self.token = token

	def upload(self) :

		if not os.path.exists("output/extensions/tmp"):
				os.mkdir("output/extensions/tmp")

		dbx = dropbox.Dropbox(self.token)

		directory = "output/extensions/{}".format(self.extension)
		zipile = "output/extensions/tmp/{}{}".format(self.extension, ".zip")

		
		for dirname, subdirs, files in os.walk(directory):
			zf = zipfile.ZipFile(zipile, "a", zipfile.ZIP_DEFLATED)
			for filename in files:
				zf.write(os.path.join(dirname, filename))
			zf.close()

		overwrite = True
		
		if overwrite:
			mode = dropbox.files.WriteMode.overwrite

		for dirname, subdirs, files in os.walk(directory):
			mtime = os.path.getmtime(zipile)
			with open(zipile, "rb") as f :
				data = f.read()
				try:
					res = dbx.files_upload(data, "/Downloads/{}{}".format(self.extension, ".zip"), mode=mode)
					f.close()
				except dropbox.exceptions.ApiError as e:
					raise e
			print('uploaded as', res.name.encode('utf8'))
   
