import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def ask_gemini(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, I had trouble processing that."