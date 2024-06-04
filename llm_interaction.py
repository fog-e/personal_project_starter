import openai
import os

# Access the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
