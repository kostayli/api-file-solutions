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


```
docker-compose up --build
```
Client configurations are described in settings.conf.
## Example:
If the address is not specified, it is taken from the settings.conf file.
Structure settings.conf:
```
[Settings]
host = 127.0.0.1
port = 8008
```
### get_list
```
clients get_list
clients 127.0.0.1:8008 get_list
```

### get_file
```
clients get_file <NameFile> <NamePath>
clients 127.0.0.1:8008 get_file <NameFile> <NamePath>
```
NameFile - parameter of the name of the file to download\
NamePath - the parameter of the name of the directory where the download will be performed

 ### upload
```
clients upload <NameFile> 
clients 127.0.0.1:8008 upload <NameFile> 
```
NameFile - parameter of the path of the file for uploading on server
  
### update
```
clients update <NameFile> 
clients 127.0.0.1:8008 update <NameFile> 
```
NameFile - parameter of the path of the file for updating on serve
  
### delete
```
clients delete <NameFile> 
clients 127.0.0.1:8008 delete <NameFile> 
```
NameFile - parameter of the path of the file for deleting on serve
