from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pyresparser import ResumeParser
import shutil
import json

app = FastAPI()

@app.post('/parse_resume')
def upload_file(uploaded_file: UploadFile = File(...)):
    path = f"files/{uploaded_file.filename}"
    with open(path, 'w+b') as file:
        shutil.copyfileobj(uploaded_file.file, file)
    data = ResumeParser(path).get_extracted_data()
    data = json.dumps(data).encode('utf8')
    return data

#CURL to test the API: 
#curl.exe -X POST http://127.0.0.1:8000/parse_resume -H "Content-Type: multipart/form-data" -F "uploaded_file=@C://YOUR_PATH/YOURFILE.pdf;type=application/pdf" 