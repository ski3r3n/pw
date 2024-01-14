from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openaiapikey = os.getenv("OPENAIAPIKEY")

c = OpenAI(api_key=openaiapikey)
audio_file = open("Recording(4).m4a", "rb")

transcript = c.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text",
    prompt="answer in english"
)

print(f"\n\nChatGPT:\n{transcript}")

client = OpenAI(api_key=openaiapikey)

# temprompt = input("Your prompt: ")
lang = input('what language u answer in: ')
longprompt = '''

'''
audioprompt = str(transcript) + f"answer in {lang}"
#
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You always answer in english. You sumarise teacher's lectures for students to understand. You make sure to include important points. Summarise whatever prompt is given, in bullet point format, ranked from most important to least important. Answer in english."},
        {"role": "user", "content": audioprompt}
    ]
)

print(f"\n\nChatGPT:\n{completion.choices[0].message.content}")
