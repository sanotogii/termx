import google.generativeai as genai
from config import Config
import readline

config = Config()

generation_config = config.generation_config
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  
)

chat_session = model.start_chat(
  history=[
  ]
)

chat_history = []
chat_counter = 0

try:
    while True:
        input_msg = input("> ")
        msg =input_msg + ", keep it short, OS=UBUNTU, no markdown, if steps use ordered list, do not be very specific"
        if input_msg:
            readline.add_history(msg)
        response = chat_session.send_message(msg)
        
        if msg.startswith("/help"):
            print("/q: quit")
        elif msg.startswith("/q" or "/quit"):
            print("\nbye!")
            break
        else:
            print(response.text)
            chat_history+=input_msg
except KeyboardInterrupt:
    print('\nbye!')