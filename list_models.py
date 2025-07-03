import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")

genai.configure(api_key=api_key)

def list_available_models():
    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"- {model.name}")

if __name__ == "__main__":
    list_available_models()
