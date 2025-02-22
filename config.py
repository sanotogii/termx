import os
import google.generativeai as genai
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables")    

        genai.configure(api_key=self.GEMINI_API_KEY, transport='rest')

        self.generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 65536,
        "response_mime_type": "text/plain",
        }
