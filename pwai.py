from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openaiapikey = os.getenv("openaiapikey")
client = OpenAI(api_key=openaiapikey)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You sumarise teacher's lectures for students to understand. You make sure to include important points."},
        {"role": "user", "content": """This is the story of how Feynman's lost lecture
came to be lost, and how it came to be found
again. In April 1992, as Caltech's archivist, I was
asked by Gerry Neugebauer, the chairman of the
Division of Physics, Mathematics and Astronomy, to go through the files in Robert Leighton's
office. Leighton was ill and had not used his
office for several years. Marge Leighton, his wife,
had told Neugebauer that it was all right to clean
out the office-she'd already collected her husband's books and personal effects. I could take
what I wanted for the archives, and the division
would dispose of the rest. """}
    ]
)

print(completion.choices[0].message)
