import openai
import os


def generate_summary(text):
    """Generate summary using GPT-3 API"""
    openai.api_key = os.getenv("API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=text, max_tokens=100, temperature=0.7
    )
    summary = response.choices[0].text.strip()
    return summary
