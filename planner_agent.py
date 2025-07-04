import os
import google.generativeai as genai
from dotenv import load_dotenv

from openai import AsyncOpenAI
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables!")

genai.configure(api_key=api_key)

# Use a powerful text generation model from your list
model = genai.GenerativeModel("models/gemini-2.5-pro")

def generate_health_plan(user_input: str) -> str:
    prompt = f"""
You are a friendly and professional health and wellness assistant.
The user said: "{user_input}"

Based on this goal, create a detailed and motivational health plan that includes:
1. A personalized diet plan (breakfast, lunch, dinner)
2. A workout routine (with home and gym options)
3. Weekly goal tracking and encouragement tips

Format the response clearly using headings and bullet points.
"""
    response = model.generate_content(prompt)
    return response.text
