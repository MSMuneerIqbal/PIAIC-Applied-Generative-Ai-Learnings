
from litellm import completion
import os

## set ENV variables
os.environ["GEMINI_API_KEY"] = "AIzaSyAKbche_LIP23hXp1YCjXHFXNCBZEGRHy0"
def call_gemini():
  response = completion(
  model="gemini/gemini-1.5-flash",
  messages=[{ "content": "what are ai agents","role": "user"}]
  )
  print(response['choices'][0]['message']['content'])