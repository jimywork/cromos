#!/usr/bin/python

import os
import shutil
import json

# Class para tratar alguns erros e remover pastas que geram erros quando fazem o deploy
class Errors :

	def __init__(self, extension) :
		self.extension = extension

	
	def removeFolders(self, extension) :

		metadata = "{}/_metadata".format(extension)
		folders = [metadata] # Array com as pastas que deveram ser retiradas

		for folder in folders :
			if os.path.exists(folder) and os.path.isdir(folder):
				shutil.rmtree(folder)

	def removeKeys(self, extension) :

		try:

			minefest = "{}/manifest.json".format(extension)
			keys = ["update_url"] # Array com as keys que deveram ser retiradas

			with open(minefest, 'rb') as f :
				manifest = json.load(f)

				for key in keys :
					if key in manifest.keys():

						manifest.pop(key, None)

						with open(minefest, 'wb') as j :
							j.write(json.dumps(manifest, indent=2, sort_keys=True, separators=(',', ': '), ensure_ascii=False)) 
							j.close()
			f.close()
		except IOError as e:
			print(e)