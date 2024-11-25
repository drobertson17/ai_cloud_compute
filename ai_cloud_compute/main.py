import base64
from fastapi import FastAPI, File, UploadFile
from uuid import uuid4

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# def image_to_base64(self, img_path: str) -> str:
#     """Converts a local image file to base64 string."""
#     with Image.open(img_path) as img:
#         buffered = BytesIO()
#         img.save(buffered, format="PNG")
#         img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
#     return img_str

@app.post("/image-description")
async def image_description(file: UploadFile = File()):
    file.filename = f"{uuid4()}.jpg"
    contents = await file.read()  # <-- Important!
    img_str = base64.b64encode(contents).decode("utf-8")
    return img_str
