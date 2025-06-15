from openai import OpenAI
import os
from dotenv import load_dotenv  # You might need to: pip install python-dotenv

load_dotenv()  # This loads your .env file
def promptLLM(question, contextInfo):
    key=os.getenv("OPENROUTER_API_KEY")  # Ensure you have your API key in .env file
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key,
    )

    completion = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert sports analyst AI focused on NFL football!! [CHANGESSSSSSS]"
                    "You analyze past team records to find trends, strengths, weaknesses, and predict future performance. "
                    "Use the context to support your prediction."
                ),
            },
            {
                "role": "system",
                "content": (
                    "Context: This is a list of recent win-loss records for NFL teams. "
                    "Use this data to help generate predictions and performance summaries:\n" + str(contextInfo)
                ),
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return completion.choices[0].message.content