
$URL = "******"
$FILE = "C:\chrome.zip"

Function Get-Webfile ($url)
{
 (new-object net.webclient).DownloadFile($url,'chrome.zip')
}

Function Get-Unzip ($file) {
    Expand-Archive -Path $file -DestinationPath "C:\chrome"
}

Get-Webfile($URL)
Get-Unzip($FILE)