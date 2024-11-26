from pydantic import BaseModel


class ImageDescriptionSummary(BaseModel):
    short_desc: str
    title: str
    keywords: str
    classification: str