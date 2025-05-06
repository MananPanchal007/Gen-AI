from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        { "role": "user", "content": "What is greator? 9.8 or 9.11" } # Zero Shot Prompting
    ]
)

print(result.choices[0].message.content)


# *************Gemini zero shot prompting**************

from google import genai
from google.genai import types

client = genai.Client(api_key='Your API key here')

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents='Why is the sky blue?' # Zero Shot Prompting
)
print(response.text)
