import google.generativeai as genai
from config import Config
import readline
import os

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


try:
    while True:
        input_msg = input("❯ ")
        msg =input_msg + ", keep it short, OS=UBUNTU, no markdown, if steps use ordered list, do not be very specific, give cli solutions"
        if input_msg:
            readline.add_history(input_msg)
        response = chat_session.send_message(msg)
        
        if msg.startswith("/help"):
            print("/q: quit")
        elif msg.startswith("clear"):
            os.system("clear")
        elif msg.startswith("/q" or "/quit"):
            print("bye!")
            break
        else:
            print(response.text)
except KeyboardInterrupt:
    print('bye!')