import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def planner(user_text, memory):
    prompt = f"""
    वापरकर्ता मराठीत बोलत आहे.
    उपलब्ध माहिती: {memory.data}

    पुढील कृती ठरवा:
    1. अधिक माहिती विचारायची?
    2. पात्रता तपासायची?
    3. योजना सांगायची?

    वापरकर्ता: {user_text}
    """
    response = model.generate_content(prompt)
    return response.text
