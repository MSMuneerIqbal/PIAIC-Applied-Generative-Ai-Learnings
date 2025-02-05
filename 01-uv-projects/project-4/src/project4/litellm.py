from litellm import completion
import os

## set ENV variables
os.environ["GEMINI_API_KEY"] = ""
def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "who is founder of pakistan","role": "user"}]
    )

    print(response['choices'][0]['message']['content'])
