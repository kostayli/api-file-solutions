import configparser
import os
import sys

import requests
from requests import RequestException, Response

host_port: str = ''


def crud_config(path) -> str:
    if not os.path.exists(path):
        return "HeOk"
    config = configparser.ConfigParser()
    config.read(path)
    host = config.get("Settings", "host")
    port = config.get("Settings", "port")
    return host + ":" + port


try:
    if sys.argv[1].__contains__(':'):
        host_port = sys.argv[1]
    else:
        host_port = crud_config('settings.conf')
except:
    print(f"Error!!!")


def get_list_file() -> None:
    url: str = 'http://' + host_port + '/get_list_files'
    response: Response = requests.get(url=url)
    result: dict[str: str] = response.json()
    if len(result) == 0:
        print("No files on directory!")
    for data in result:
        print("Filename: " + data + ", Hash: " + result[data])


def get_file(name: str, path: str) -> None:
    url: str = 'http://' + host_port + '/get__file?name=' + name
    response = requests.get(url=url, stream=True)
    if response.status_code == 200:
        path_dir_name: list[str] = path.split('/')
        for i in path_dir_name:
            if i.__contains__('.'):
                path_dir_name.remove(i)
        if not os.path.exists('/'.join(path_dir_name)) and len(path_dir_name) != 0:
            os.makedirs('/'.join(path_dir_name))
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        print('Ok')
    else:
        print('HeOk')


def upload(path: str) -> None:
    url: str = 'http://' + host_port + '/upload'
    try:
        file: dict[str: any] = {'file': open(path, 'rb')}
        response: Response = requests.put(url=url, files=file)
        if response.status_code == 200:
            print('Ok')
        else:
            print('HeOk')
    except:
        print('HeOk')


def update(path: str) -> None:
    url: str = 'http://' + host_port + '/update'
    try:
        file: dict[str: any] = {'file': open(path, 'rb')}
        response: Response = requests.post(url=url, files=file)
        if response.status_code == 200:
            print('Ok')
        else:
            print('HeOk')
    except:
        print('HeOk')


def delete_file_from_server(path: str) -> None:
    url: str = 'http://' + host_port + '/remove_file?file=' + path
    response: Response = requests.delete(url=url)
    if response.status_code == 200:
        print('Ok')
    else:
        print('HeOk')


if __name__ == '__main__':
    for param in sys.argv:
        try:
            if param == 'get_list':
                if len(sys.argv) <= 3:
                    get_list_file()
                else:
                    print("Error param!!!")
            elif param == 'get_file':
                if len(sys.argv) == 5:
                    get_file(sys.argv[3], sys.argv[4])
                else:
                    get_file(sys.argv[2], sys.argv[3])
            elif param == 'upload':
                if len(sys.argv) == 4:
                    upload(sys.argv[3])
                else:
                    upload(sys.argv[2])
            elif param == 'update':
                if len(sys.argv) == 4:
                    update(sys.argv[3])
                else:
                    update(sys.argv[2])
            elif param == 'delete':
                if len(sys.argv) == 4:
                    delete_file_from_server(sys.argv[3])
                else:
                    delete_file_from_server(sys.argv[2])
        except RequestException:
            print(f"Error connection!!!")
            break
        except:
            print("Error!!!")
