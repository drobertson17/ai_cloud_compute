def image_description_prompt(image) -> list[dict]:
    return [
        {"role": "system", "content": "You are an assistant who perfectly describes images."},
        {
            "role": "user",
            "content": [
                {"type" : "text", "text": "Describe the following image in a paragraph."},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image}"} 
            ]
        }
    ]


def title_generation_prompt(description) -> str:
    return (
        "Prompt:\Create a concise, descriptive title for an image based on "
        "the following detailed description. Only provide the title—no "
        "additional text or explanation. Keep the title matter-of-fact. For example:\n\n"
        "[EXAMPLE]\n\n"
        "IMAGE DESCRIPTION:\n"
        "The image features a wooden pathway in a lush green field, surrounded "
        "by a beautiful landscape. The pathway is lined with grass.\n\n"
        "YOUR RESPONSE:\n"
        "Title: Wooden Pathway"
        "\n\n[/EXAMPLE]\n\n"
        f"\n\nIMAGE DESCRIPTION:\n{description}\n\n"
        "YOUR RESPONSE:\n"
    )

def summary_generation_prompt(description) -> str:
    return (
        "Prompt:\Create a concise, descriptive summary based on "
        "the following detailed description. Only provide the summary—no "
        "additional text or explanation. Keep the text matter-of-fact. For example:\n\n"
        "[EXAMPLE]\n\n"
        "IMAGE DESCRIPTION:\n"
        "The image features a wooden walkway or bridge, surrounded by a lush "
        "green field with tall grass. The pathway is located in the middle of "
        "the field, providing a connection between different areas. The sky above "
        "the field is blue, and the overall atmosphere appears serene and peaceful. "
        "The scene is reminiscent of a park or a countryside setting, where one can "
        "enjoy a leisurely walk or a quiet moment of reflection.'.\n\n"
        "YOUR RESPONSE:\n"
        "Summary: The image features a wooden pathway in a lush green field, surrounded "
        "by a beautiful landscape. The pathway is lined with grass"
        "\n\n[/EXAMPLE]\n\n"
        f"\n\nIMAGE DESCRIPTION:\n{description}\n\n"
        "YOUR RESPONSE:\n"
    )

def keyword_generation_prompt(description) -> str:
    return (
        "Prompt:\Create a concise, descriptive list of keywords based on "
        "the following detailed description. Only provide the keywords—no "
        "additional text or explanation. For example:\n\n"
        "[EXAMPLE]\n\n"
        "IMAGE DESCRIPTION:\n"
        "The image features a wooden walkway or bridge, surrounded by a lush "
        "green field with tall grass. The pathway is located in the middle of "
        "the field, providing a connection between different areas. The sky above "
        "the field is blue, and the overall atmosphere appears serene and peaceful. "
        "The scene is reminiscent of a park or a countryside setting, where one can "
        "enjoy a leisurely walk or a quiet moment of reflection.'.\n\n"
        "YOUR RESPONSE:\n"
        "Keywords: Grass, nature, pathway"
        "\n\n[/EXAMPLE]\n\n"
        f"\n\nIMAGE DESCRIPTION:\n{description}\n\n"
        "YOUR RESPONSE:\n"
    )


def classification_prompt(description) -> str:
    return (
        "Prompt: Select one of the following options to classify the image based on "
        "it's description:\n"
        " 1. Natural/landscape\n"
        " 2. Picture of building or structure\n"
        " 3. Selfie\n"
        " 4. Friends and Family Picture\n"
        " 5. None of the above\n\n"
        "[EXAMPLE]\n\n"
        "IMAGE DESCRIPTION:\n"
        "The image features a wooden walkway or bridge, surrounded by a lush "
        "green field with tall grass. The pathway is located in the middle of "
        "the field, providing a connection between different areas. The sky above "
        "the field is blue, and the overall atmosphere appears serene and peaceful. "
        "The scene is reminiscent of a park or a countryside setting, where one can "
        "enjoy a leisurely walk or a quiet moment of reflection.'.\n\n"
        "YOUR RESPONSE:\n"
        "1"
        "\n\n[/EXAMPLE]\n\n"
        f"\n\nIMAGE DESCRIPTION:\n{description}\n\n"
        "YOUR RESPONSE:\n"
    )