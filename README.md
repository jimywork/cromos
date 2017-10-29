# Cromos 

Cromos is a tool for downloading legitimate extensions of the Chrome Web Store and inject codes in the background of the application and more cromos create executable files to force installation via <strong>PowerShell</strong> or <strong>VBScript</strong> for example, and also upload files to dropbox to host the malicious files.

  - Download extension
  - Injections
  - Upload files on dropbox
  

  
  ### Demo
  This is a demonstration of the tool at work in this examples I'm downloading a famous Google extension called idkloemkmldbemijiamdiolojbffnjlh on Google Chrome Web Store and injecting a mining module.
  
  
<a href="https://asciinema.org/a/A5lqt8S2bAuWtpOzYsfauwLsv?autoplay=1"><img src="https://asciinema.org/a/A5lqt8S2bAuWtpOzYsfauwLsv.png"/></a>
  
  ### Installation
  
```
$ cd $HOME/
$ git clone https://github.com/fbctf/cromos
$ sudo chmod -R 777 cromos/
$ cd cromos && python setup.py
```
 ### Usage
 ```
 
Usage: python cromos.py --extension {id} --load {keylogger/currency} --build {.bat, .vbs} --token {token}
 ```
 
### Modules
You can also inject some predefined modules in the background as <strong>keylogger</strong>, <strong>virtual currency</strong>.

Module | Description
--------|------------
modules/keylogger | This module captures all the passwords you type in an infected browser over https or not.
modules/currency | This module allows you to mine virtual coins using the coinhive API, you just need to have an account.
