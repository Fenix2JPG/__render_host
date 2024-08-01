#pip install -q -U google-generativeai

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


API_KEY_IA = os.getenv('API_KEY_IA')

import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key = API_KEY_IA)


class Ia():
    def __init__(self) -> None:
        model = genai.GenerativeModel("gemini-pro")
        self.chat = model.start_chat(history=[])
    def send_message(self,message):
        try:
            ia_message = self.chat.send_message(message)
            ia_message = ia_message.candidates[0].content.parts[0].text
            print(ia_message)
            return ia_message
        except:
            return "..."
 

