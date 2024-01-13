from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openaiapikey = os.getenv("OPENAIAPIKEY")
client = OpenAI(api_key=openaiapikey)

temprompt = input("Your prompt: ")

longprompt = '''

'''
#
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You sumarise teacher's lectures for students to understand. You make sure to include important points. Summarise whatever prompt is given, in bullet point format, ranked from most important to least important"},
        {"role": "user", "content": temprompt}
    ]
)

print(f"\n\nChatGPT:\n{completion.choices[0].message.content}")
