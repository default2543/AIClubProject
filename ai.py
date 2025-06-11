from openai import OpenAI

def promptLLM(question, contextInfo):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="sk-or-v1-190d9ebd7a3c4d956bb091b5f" \
                "28ae480b9b568758cd3b5203cebf5a4d5b6e300",
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