# Cromos 

Chrome is a tool for downloading legitimate extensions of the Chrome Web Store and inject codes in the background of the application and more chrome create executable files to force installation via powershell or vbscript for example and also upload files to google drive for host the malicious files.

  - Download extension
  - Injections
  - Upload on google drive
  
  ### Demo
  This is a demonstration of the tool at work in this examples I'm downloading a famous Google extension called Alert Password on Google Chrome Web Store.
  
  ### Installation
  
```
$ cd /path/folder/
$ git clone https://github.com/fbctf/cromos
$ cd cromos && python setup.py
```
 ### Usage
 ```
 
Usage: python cromos.py --extension {id} --load {keylogger} --build {.bat}

         (         )      *         )    (     
   (     )\ )   ( /(    (  `     ( /(    )\ )  
   )\   (()/(   )\())   )\))(    )\())  (()/(  
 (((_)   /(_)) ((_)\   ((_)()\  ((_)\    /(_)) 
 )\___  (_))     ((_)  (_()((_)   ((_)  (_))   
((/ __| | _ \   / _ \  |  \/  |  / _ \  / __|  
 | (__  |   /  | (_) | | |\/| | | (_) | \__ \  
  \___| |_|_\   \___/  |_|  |_|  \___/  |___/
 
  Version: 1.0 Builds: 3 Modules: 2
  
optional arguments:
  -h, --help            show this help message and exit
  --extension EXTENSION
                        Download a extension from Google Chrome Webstore
  --load LOAD           Load a module to run in background with the
                        application
  --build BUILD         Build types .bat .exe .vbs
  --key KEY             API key for uploading files in Google Drive
  
 ```
