import os
from openai import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

api_key='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'

chat = ChatOpenAI(
  model_name="gpt-3.5-turbo",
  temperature=0,
  openai_api_key=api_key,
  streaming=True,
  callbacks=[StreamingStdOutCallbackHandler()]
)

messages = [
  HumanMessage(content="自己紹介してください")
]
result = chat(messages)
print(result.content)