import hashlib
import os
from os import listdir
from os.path import isfile
from os.path import join
from typing import AnyStr

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask

app = FastAPI()


def custom_openapi() -> dict[str: any]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema: dict[str: any] = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get('/get_list_files')
def get_list_files() -> dict[str: str]:
    list_files: list[str] = [f for f in listdir("./tmp") if isfile(join("./tmp", f))]
    result: dict[str: str] = {}
    for name in list_files:
        result[name] = (hashlib.md5(open("./tmp/" + name, 'rb').read()).hexdigest())
    return result


@app.get('/get__file')
def get_file(name: str) -> FileResponse:
    return FileResponse(path="./tmp/" + name, filename=name, media_type='multipart/form-data')


@app.put('/upload')
def upload(file: UploadFile = File(...)) -> dict[str: str]:
    try:
        contents = file.file.read()
        bool_param: bool = os.path.exists("./tmp/" + file.filename)
        if bool_param:
            return {"message": "There was an error uploading the file"}
        else:
            with open("./tmp/" + file.filename, 'wb') as f:
                f.write(contents)
    except Exception:
        raise HTTPException(403, detail="There was an error uploading the file")
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}


@app.post('/update')
def update(file: UploadFile = File(...)) -> dict[str: str]:
    try:
        contents: AnyStr = file.file.read()
        bool_param: bool = os.path.exists("./tmp/" + file.filename)
        if bool_param:
            if (hashlib.md5(open("./tmp/" + file.filename, 'rb').read()).hexdigest() == hashlib.md5(
                    contents).hexdigest()):
                raise HTTPException(403, detail="A similar file is already available on the server")
            else:
                with open("./tmp/" + file.filename, 'wb') as f:
                    f.write(contents)
        else:
            with open("./tmp/" + file.filename, 'wb') as f:
                f.write(contents)
    except Exception:
        raise HTTPException(403, detail="There was an error uploading the file")
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}


def cleanup(temp_file: str):
    os.remove("./tmp/" + temp_file)


@app.delete('/remove_file')
def delete_file(file: str) -> FileResponse:
    try:
        return FileResponse(
            "./tmp/" + file,
            background=BackgroundTask(cleanup, file),
        )
    except Exception:
        raise HTTPException(403, detail='The file is missing in the directory')
