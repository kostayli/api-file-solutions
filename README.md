# Server
## Code downloading
```
git clone https://github.com/kostayli/api-file-solutions.git
```
## docker-compose
In the root directory of the project, you need to open a terminal.
This can be done in the following ways:
- Win + R. In the field that opens, type "cmd" and press enter.
cd projectPath - where porjectPath is the path to the project folder
- Right-click in the root folder->Open Command Window(PowerShell).

```
docker-compose up --build
```
Server configurations are described in dockerfile and docker-compose.yml. 

# Client
## Code downloading
Download clients : https://github.com/kostayli/api-file-solutions/releases/download/v1.0/clients.zip

Client configurations are described in settings.conf.
## Example:
If the address is not specified, it is taken from the settings.conf file.
Structure settings.conf:
```
[Settings]
host = 127.0.0.1
port = 8008
```
### get_list_file
```
clients get_list_file
clients get_list_file <Host:Port>
```
### get_file
```
clients get_file <NameFile> <NamePath>
clients get_file <NameFile> <NamePath> <Host:Port>
```
NameFile - parameter of the name of the file to download\
NamePath - the parameter of the name of the directory where the download will be performed

 ### upload
```
clients upload <NameFile> 
clients upload <NameFile> <Host:Port>
```
NameFile - parameter of the path of the file for uploading on server
  
### update
```
clients update <NameFile> 
clients update <NameFile> <Host:Port>
```
NameFile - parameter of the path of the file for updating on serve
  
### delete
```
clients delete <NameFile> 
clients delete <NameFile> <Host:Port>
```
NameFile - parameter of the path of the file for deleting on serve

## Documentation
```
http://localhost:8008/redoc 
http://localhost:8008/docs
```
