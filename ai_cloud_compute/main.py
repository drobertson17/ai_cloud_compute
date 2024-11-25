from fastapi import FastAPI, File, UploadFile
from uuid import uuid4

from ai_cloud_compute.models import describe_image_contents

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image-description")
async def image_description(file: UploadFile = File()):
    file.filename = f"{uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    return describe_image_contents(contents)

