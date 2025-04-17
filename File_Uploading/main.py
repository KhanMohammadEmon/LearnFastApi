from fastapi import FastAPI,File,UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse

app = FastAPI()




@app.post("/")
async def main(file: Annotated[bytes,File()]):
    print(file)
    return {"Hello": "World"}

@app.post("/upload")
async def upload(files: UploadFile):
    # if files.content_type != "image/jpeg" and files.content_type != "image/png" and files.content_type != "image/jpg":
    #     return {"error": "Image file only allowed"}
    
    # with open(files.filename, "wb") as f:
    #     f.write(files.file.read())
    #     return "File Uploaded Successfully"
    
    filePath = files.filename
    fileContent = files.file.read()
    
    f = open(filePath, "wb")
    try:
        f.write(fileContent)
        return "File Uploaded Successfully"
    except Exception as e:
        return {"error": str(e)}
    finally:
        f.close()
        
        
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/upload/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
        
