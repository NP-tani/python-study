import os
from openai import OpenAI

client = OpenAI(api_key='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')

response = client.chat.completions.create(model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! I'm John. "}
  ],
  stream=True
)

for chunk in response:
  choice = chunk.choices[0]
  if choice.finish_reason is None and hasattr(choice.delta, "content"):
    print(choice.delta.content)
