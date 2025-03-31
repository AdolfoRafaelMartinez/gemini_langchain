from dotenv import load_dotenv

import os
from IPython.display import display
from IPython.display import Markdown
import textwrap

import google.generativeai as genai

load_dotenv()

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name = "gemini-2.0-flash")
prompt_parts = [
    "Write a Python function and explain it to me",
]
response = model.generate_content(prompt_parts)

print(response.text)