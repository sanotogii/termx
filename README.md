# CLI Chat Assistant

A command-line interface chatbot powered by Google's Gemini AI.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install google-generativeai python-dotenv readline
```
3. Create a `.env` file in the project root and add your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the application:
```bash
python app.py
```

### Commands
- Type your message and press Enter to chat
- `/help` - Show available commands
- `/q` or `/quit` - Exit the application
- `clear` - Clear the screen

## Configuration

The chat behavior can be modified by adjusting the generation parameters in `config.py`:
- temperature
- top_p
- top_k
- max_output_tokens
