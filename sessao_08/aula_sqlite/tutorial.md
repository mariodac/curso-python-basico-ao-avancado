## Tutorial oficial:
https://learn.microsoft.com/en-us/windows/wsl/install
### Passo 1 (PowerShell Admin):
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
### Passo 2 (PowerShell Admin):
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
### Passo 3
REINICIE O COMPUTADOR
### Passo 4 (Download the Linux kernel update package):
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
### Passo 5 (PowerShell Admin):
wsl --set-default-version 2
# # Passo 7 (Instale o docker):
Tutorial: https://docs.docker.com/docker-for-windows/install/