import base64
from lmdeploy import pipeline

VLM = pipeline('liuhaotian/llava-v1.6-vicuna-7b')
VLM_SYSTEM_MESSAGE = "You are an assistant who perfectly describes images."
VLM_USER_PROMPT = "Describe the following image in a paragraph."


def describe_image_contents(image_data_b64: str):
    img_base64 = base64.b64encode(image_data_b64).decode("utf-8")
    
    messages = [
        {"role": "system", "content": VLM_SYSTEM_MESSAGE},
        {
            "role": "user",
            "content": [
                {"type" : "text", "text": VLM_USER_PROMPT},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{img_base64}"} 
            ]
        }
    ]
    print(messages)

    return VLM(messages)