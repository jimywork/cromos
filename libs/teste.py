#!/usr/bin/python

import os
import dropbox
from dropbox.exceptions import ApiError

drivebox = dropbox.Dropbox("HNXARl-HuUAAAAAAAAAA812r0clQU9nsQgMsD0AQht5GznJaCOWNbtWp_-CU-Lrl")

files = drivebox.files_list_folder('/Extensions')

for file in files.entries:

	if "gkljgfmjocfalijkgoogmfffkhmkbgol" in file.path_lower:
			try:
				shared = drivebox.sharing_create_shared_link_with_settings(file.path_lower)
				print(shared.url)
			except ApiError as err:
				if err.error.is_shared_link_already_exists() :
					print("{} Link already exists".format("[!]"))
				if err.error.is_path() and err.error.get_path().is_not_found() :
					print("{} File not found".format("[!]"))
				elif err.error.is_settings_error():
					print(err.error.get_settings_error())