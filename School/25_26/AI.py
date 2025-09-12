from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API")  # Read the key from your .env file
if not api_key:
    raise ValueError("GEMINI_API not set in environment")

client = genai.Client(api_key=api_key)

while True:
    word = input("Enter a word (or 'quit' to exit): ").strip()
    if word.lower() == "quit":
        break

    prompt = f"Define the word '{word}' in simple terms."

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    print("Definition:", response.text.strip())

