from django.shortcuts import render
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def home(request):
    summary = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful study assistant."},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=300
            )
            summary = response.choices[0].message.content
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render(request, "assistant/home.html", {"summary": summary})
