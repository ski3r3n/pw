from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openaiapikey = os.getenv("OPENAIAPIKEY")

c = OpenAI(api_key=openaiapikey)
audio_file = open("Recording(5).m4a", "rb")

transcript = c.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text",
)

print(f"\n\nChatGPT:\n{transcript}")

client = OpenAI(api_key=openaiapikey)

# temprompt = input("Your prompt: ")
lang = input('what language do you want the answer in: ')

longprompt = '''

'''
style = input("styling (point form, short paragraph, long essay): ")

audioprompt = str(transcript) + f"answer in {lang}"
#
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You sumarise teacher's lectures for students to understand. You make sure to include important points. Summarise whatever prompt is given, in {style} format, ranked from most important to least important."},
        {"role": "user", "content": audioprompt}
    ]
)

print(f"\n\nChatGPT:\n{completion.choices[0].message.content}")
