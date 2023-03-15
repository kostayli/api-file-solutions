import configparser
import os
import sys

import requests
from requests import Response, RequestException
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def crud_config(path) -> str:
    if not os.path.exists(path):
        return "HeOk"
    config = configparser.ConfigParser()
    config.read(path)
    host = config.get("Settings", "host")
    port = config.get("Settings", "port")
    return host + ":" + port


def get_list_file(host_port: str = crud_config('settings.conf')) -> dict[str: str]:
    url: str = 'http://' + host_port + '/get_list_files'
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response: Response = requests.get(url=url)
    result: dict[str: str] = response.json()
    if len(result) == 0:
        print("No files on directory!")
    for data in result:
        print("Filename: " + data + ", Hash: " + result[data])
    return result


def get_file(name: str, path: str, host_port: str = crud_config('settings.conf')) -> int:
    url: str = 'http://' + host_port + '/get__file?name=' + name
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
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
        return 1
    else:
        print('HeOk')
        return 0


def upload(path: str, host_port: str = crud_config('settings.conf')) -> int:
    url: str = 'http://' + host_port + '/upload'
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    try:
        file = open(path, 'rb')
        file_to_upload: dict[str: any] = {'file': file}
        response: Response = requests.put(url=url, files=file_to_upload)
        file.close()
        if response.status_code == 200:
            print('Ok')
            return 1
        else:
            print('HeOk')
            return 0
    except:
        print('HeOk')
        return 0


def update(path: str, host_port: str = crud_config('settings.conf')) -> int:
    url: str = 'http://' + host_port + '/update'
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    try:
        file = open(path, 'rb')
        file_to_update: dict[str: any] = {'file': file}
        response: Response = requests.post(url=url, files=file_to_update)
        file.close()
        if response.status_code == 200:
            print('Ok')
            return 1
        else:
            print('HeOk')
            return 0
    except:
        print('HeOk')
        return 0


def delete(path: str, host_port: str = crud_config('settings.conf')) -> int:
    url: str = 'http://' + host_port + '/remove_file?file=' + path
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response: Response = requests.delete(url=url)
    if response.status_code == 200:
        print('Ok')
        return 1
    else:
        print('HeOk')
        return 0


if __name__ == '__main__':
    try:
        if len(sys.argv) == 5:
            globals()[sys.argv[1]](sys.argv[2], sys.argv[3], sys.argv[4])
        elif len(sys.argv) == 4:
            globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            globals()[sys.argv[1]](sys.argv[2])
        elif len(sys.argv) == 2:
            globals()[sys.argv[1]]()
        else:
            print("Error param!!!")
    except RequestException:
        print(f"Error connection!!!")
    except:
        print("Error!!!")
