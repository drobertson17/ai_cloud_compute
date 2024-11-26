import uvicorn
from fastapi import FastAPI, File, UploadFile

from ai_cloud_compute.schemas import ImageDescriptionSummary
from ai_cloud_compute.models import describe_image_contents, summarize_image_description


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/image-description", response_model=str)
async def image_description(image_file: UploadFile = File()) -> str:
    image = await image_file.read()  # <-- Important!
    return describe_image_contents(image)


@app.post("/image-summary", response_model=ImageDescriptionSummary)
async def image_description(full_description: str) -> ImageDescriptionSummary:
    return summarize_image_description(full_description)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)