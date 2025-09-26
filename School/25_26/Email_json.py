from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load variables from .env
load_dotenv()

# Read the key from environment
API_KEY = os.getenv("GEMINI_API")
if not API_KEY:
    raise ValueError("GEMINI_API not set in .env file")

# Initialize the Gemini client
client = genai.Client(api_key=API_KEY)

# Define the LLM-generated fields (without timestamp)
llm_response_schema = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "classification": types.Schema(
            type=types.Type.STRING,
            description="The classified category of the email: support, complaint, general, promo, or spam."
        ),
        "subject": types.Schema(
            type=types.Type.STRING,
            description="A concise subject line for the generated reply."
        ),
        "body": types.Schema(
            type=types.Type.STRING,
            description="The full body of the reply, including the signature 'EasyAgents support team' and written in the original email's language. "
                        "If the email is classified as spam, this field should be empty or contain a single dash: '-'."
        ),
    },
    required=["classification", "subject", "body"],
)

def classify_and_reply(email_body: str) -> dict:
    # Capture the system timestamp *before* calling the LLM
    current_timestamp = datetime.utcnow().isoformat() + 'Z'  # UTC ISO 8601

    # Prompt
    prompt = (
        f"Analyze the following email and output a JSON object containing the classification, a subject, and the reply body. "
        f"1. Classify it as one of: support, complaint, general, promo, or spam. "
        f"2. Write a short, suitable reply in the same language as the email body. "
        f"3. Use the signature: 'EasyAgents support team'. "
        f"4. If classified as 'spam', **do not** write a reply; the 'body' field must be empty or contain only a dash ('-')."
        f"5. Create a concise 'subject' line for the reply."
        f"\n\nEmail: {email_body}"
    )

    # Call Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=llm_response_schema
        )
    )
    
    # Parse LLM output
    try:
        llm_data = json.loads(response.text)
    except json.JSONDecodeError:
        llm_data = {"classification": "error", "subject": "-", "body": "-", "raw_output": response.text}

    # Insert timestamp
    final_output = {
        "timestamp": current_timestamp,
        "classification": llm_data.get("classification"),
        "subject": llm_data.get("subject"),
        "body": llm_data.get("body"),
    }
    
    return final_output

# File to save outputs
output_file = "log.json"

# Ensure file exists
if not os.path.exists(output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        pass

while True:
    email_body = input("Paste email body (or type 'quit' to exit): ")
    if email_body.lower() == "quit":
        break
    print("\n--- LLM Output (JSON) ---")
    try:
        result = classify_and_reply(email_body)
        print(json.dumps(result, indent=2))

        # Append entry to file, one key per line
        with open(output_file, "a", encoding="utf-8") as f:
            f.write("{\n")
            for k, v in result.items():
                f.write(f'  "{k}": {json.dumps(v, ensure_ascii=False)}\n')
            f.write("}\n\n")

        print(f"✅ Saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-------------------------\n")

