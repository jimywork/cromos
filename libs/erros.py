
import os
import shutil
import json


# Class to handle some errors and remove folders that generate errors when deploying the application

class Errors :

	def __init__(self, extension) :
		self.extension = extension

	def folders(self) :

		try:
			metadata = "output/extensions/{}/_metadata".format(self.extension) # Folder that should be removed application
			folders = [metadata] # Array with folders that should be removed

			for folder in folders :
				if os.path.exists(folder) and os.path.isdir(folder):
					shutil.rmtree(folder)
		except IOError as e:
			raise e

	def keys(self) :

		try:

			path = "output/extensions/{}/manifest.json".format(self.extension)
			keys = ["update_url"] # Array with folders that should be removed

			with open(path, 'rb') as f :
				manifest = json.load(f)

				for key in keys :
					if key in manifest.keys():

						manifest.pop(key, None)

						with open(path, 'wb') as w :
							w.write(json.dumps(manifest, indent=2, sort_keys=True, separators=(',', ': '), ensure_ascii=False)) 
							w.close()
			f.close()
		except IOError as e:
			raise e