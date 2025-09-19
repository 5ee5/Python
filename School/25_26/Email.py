from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API")  # Read the key from your .env file
if not api_key:
    raise ValueError("GEMINI_API not set in environment")

client = genai.Client(api_key=api_key)


def classify_and_reply(email_body: str) -> str:
    prompt = (
        "Classify this email as one of: support, complaint, general, promo, spam. "
        "Then write a short reply suited to that category."
        "You must write a reply in the same language as the email body itself"
        "Important: always try to identify the spam emails and respond 'we don't tolerate spam, Your email will be sent to bin'.\n"
        f"Email: {email_body}"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

while True:
    email_body = input("Paste email body (or type 'quit' to exit): \n")
    if email_body.lower() == "quit":
        break
    print("\n--- LLM Output ---")
    print(classify_and_reply(email_body))
    print("------------------\n")
