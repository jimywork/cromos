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

class Drive :

	def __init__(self, extension, token) :
		self.extension = extension
		self.token = token
		self.color = Colors()

	def upload(self) :

		if not os.path.exists("output/extensions/tmp"):
				os.mkdir("output/extensions/tmp")

		drivebox = dropbox.Dropbox(self.token, timeout=30)
		path = "/Extensions"

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

		print('{} Upload file in dropbox'.format(self.color.status("[+]")))

		for dirname, subdirs, files in os.walk(directory):
			mtime = os.path.getmtime(zipile)
			ctime = datetime.datetime(*time.gmtime(mtime)[:6])
			with open(zipile, "rb") as f :
				data = f.read()
				try:
					res = drivebox.files_upload(data, "{}/{}{}".format(path, self.extension, ".zip"), mode=mode, client_modified=ctime, mute=True)
					f.close()
				except dropbox.exceptions.ApiError as e:
					return None
		print('{} Upload completed files as been upload on https://www.dropbox.com/home{}'.format(self.color.status("[+]"), "{}/{}{}".format(path, self.extension, ".zip")))
		
		try:

			settings = dropbox.sharing.SharedLinkSettings(requested_visibility=dropbox.sharing.RequestedVisibility.public)
			isShared = dropbox.sharing.CreateSharedLinkWithSettingsError('shared_link_already_exists')

			# Add condition share folder

			if not isShared :
				sharedFolder = drivebox.sharing_create_shared_link(path, settings=settings)

		except dropbox.sharing.CreateSharedLinkWithSettingsError as e:
			print("{} Dropbox Error {}".format("[!]", e))
	
	def link(self) :

		drivebox = dropbox.Dropbox(self.token, timeout=30)

		link = ""
		path = drivebox.files_list_folder('/Extensions')

   		for file in path.entries:

			if self.extension in file.path_lower:
				try:
					shared = drivebox.sharing_create_shared_link_with_settings(file.path_lower).url
					shared = shared.replace("?dl=0", "?dl=1")
					link += shared
				except ApiError as err:
					if err.error.is_shared_link_already_exists() :
						print("{} Link already exists".format("[!]"))
					if err.error.is_path() and err.error.get_path().is_not_found() :
						print("{} File not found".format("[!]"))
					elif err.error.is_settings_error():
						print(err.error.get_settings_error())
		return link
