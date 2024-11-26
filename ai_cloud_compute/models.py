import base64
from lmdeploy import pipeline

from ai_cloud_compute.schemas import ImageDescriptionSummary
from ai_cloud_compute import prompts


VLM = pipeline('liuhaotian/llava-v1.6-vicuna-7b')
LLM = pipeline('internlm/internlm2_5-7b-chat')


def describe_image_contents(image_data_b64: str):
    img_base64 = base64.b64encode(image_data_b64).decode("utf-8")
    
    response = VLM(prompts.image_description_prompt(img_base64))

    return response


def summarize_image_description(description: str) -> ImageDescriptionSummary:
    prompt_list = [
        prompts.summary_generation_prompt(description),
        prompts.keyword_generation_prompt(description),
        prompts.title_generation_prompt(description),
        prompts.classification_prompt(description)
    ]

    response = LLM(prompt_list)

    return ImageDescriptionSummary(
        short_desc=response[0],
        keywords=response[1],
        title=response[2],
        classification=response[3],
    )