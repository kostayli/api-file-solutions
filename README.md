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
### get_list
```
clients get_list
```
