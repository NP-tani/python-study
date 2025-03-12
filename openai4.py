import os
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  PromptTemplate,
  SystemMessagePromptTemplate,
  HumanMessagePromptTemplate
)
from langchain.schema import HumanMessage, SystemMessage

api_key='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'

chat = ChatOpenAI(
  model_name="gpt-3.5-turbo",
  temperature=0,
  openai_api_key=api_key
)

chat_prompt = ChatPromptTemplate.from_messages([
  SystemMessagePromptTemplate.from_template("あなたは{country}料理の専門家です"),
  HumanMessagePromptTemplate.from_template("以下の料理のレシピを考えてください。\n\n料理名：{dish}")
])

messages = chat_prompt.format_messages(country="日本", dish="肉じゃが")
result = chat(messages)
print(result.content)