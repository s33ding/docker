import os
from openai import OpenAI
import config

client = OpenAI(api_key=config.KEY_ID)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Please write down five trees with their scientific names in json format."
        }
    ]
)

