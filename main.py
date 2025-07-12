import os 
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def focal():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            { "role": "user",
             "content" :  " first solo album of jungkook bts?"}
        ],
        api_key=api_key


    )
    print(response['choices'][0]['message']['content'])

if __name__ =="__main__":
     focal()
