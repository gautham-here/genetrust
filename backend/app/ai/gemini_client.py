import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


MODEL = genai.GenerativeModel("gemini-1.5-flash")


def run_gemini(prompt: str):

    try:
        response = MODEL.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"