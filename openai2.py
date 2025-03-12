import os
import json
from openai import OpenAI

client = OpenAI(api_key='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')

def get_current_waather(location, unit="celsius"):
    # Simulate fetching weather data
    weather_info = {
        "location": location,
        "temperature": "25",
        "unit": "celsius",
        "forecast": ["sunny", "windy"]
    }
    return json.dumps(weather_info)

functions = [
  {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"]
              }
          },
          "required": ["location"]
      }
  }
]

messages = [
  {"role": "user", "content": "What's the weather like in Boston?"}
]

response = client.chat.completions.create(model = "gpt-3.5-turbo",
  messages = messages,
  functions = functions
)

print(response)

response_message = response.choices[0].message

available_functions = {
  "get_current_weather": get_current_waather
}
function_name = response_message.function_call.name
function_to_call = available_functions[function_name]
function_args = json.loads(response_message.function_call.arguments)

function_response = function_to_call(
  location=function_args.get("location"),
  unit=function_args.get("unit")
)

print(function_response)