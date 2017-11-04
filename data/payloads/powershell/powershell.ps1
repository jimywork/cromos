
$URL = "******"
$FILE = Get-Location

Function Get-Webfile ($url)
{
 (new-object net.webclient).DownloadFile($url,'powershell.ps1')
}

Function Get-Unzip ($file) {
    Expand-Archive -Path $file -DestinationPath Get-Location
}

Get-Webfile($URL)
Get-Unzip($FILE)