import google.generativeai as genai
from config import Config
import readline
import os

config = Config()

SYSTEM_CONTEXT = """You are a CLI helper bot. When providing solutions:
- Keep answers short and concise
- Focus on Ubuntu terminal commands
- Avoid markdown formatting
- Use ordered lists for steps
- Provide practical CLI solutions
- Keep explanations brief"""

generation_config = config.generation_config
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  
)

chat_session = model.start_chat(
  history=[{
        "role": "user",
        "parts": [SYSTEM_CONTEXT]
    }]
)


try:
    while True:
        input_msg = input("❯ ")
        msg = input_msg
        if input_msg:
            readline.add_history(input_msg)
        

        if msg.startswith("/help"):
            print("/q: quit\nclear: self explanatory\n")
        elif msg == "":
            pass
        elif msg.startswith("clear"):
            os.system("clear")
        elif msg.startswith("/q" or "/quit"):
            print("bye!")
            break
        else:
            response = chat_session.send_message(msg)
            print(response.text)
except KeyboardInterrupt:
    print('bye!')