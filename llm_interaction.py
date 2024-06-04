import openai
import os

# Access the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()
