import os
import json
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API")
if not API_KEY:
    raise ValueError("❌ GEMINI_API not found in .env file!")

client = genai.Client(api_key=API_KEY)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def json_to_md(data, output_path):
    md = f"""# CV Evaluation Report

**Match Score:** {data['match_score']}  
**Verdict:** {data['verdict']}

## Summary
{data['summary']}

## Strengths
{"".join(f"- {s}\n" for s in data['strengths'])}

## Missing Requirements
{"".join(f"- {m}\n" for m in data['missing_requirements'])}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

def evaluate_cv(cv_path, jd_text):
    cv_text = read_file(cv_path)

    prompt = f"""
You are an HR specialist. Evaluate how well the candidate's CV matches the job description.

Job Description:
{jd_text}

Candidate CV:
{cv_text}

Respond strictly in valid JSON format:
{{
  "match_score": 0-100,
  "summary": "A short summary of how well the CV fits the JD",
  "strengths": ["Key strengths/skills matching the JD"],
  "missing_requirements": ["Important JD requirements not found in CV"],
  "verdict": "strong match | possible match | not a match"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    data = json.loads(text)
    return data

def main():
    jd_text = read_file("input_files/jd.txt")

    for i in range(1, 4):
        cv_path = f"input_files/cv{i}.txt"
        cv_folder = f"output_files/CV{i}"
        os.makedirs(cv_folder, exist_ok=True)

        json_path = f"{cv_folder}/cv.json"
        md_path = f"{cv_folder}/cv_report.md"

        print(f"\n🔍 Evaluating CV{i} ...")
        data = evaluate_cv(cv_path, jd_text)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        json_to_md(data, md_path)
        print(f"✅ Created: {json_path} and {md_path}")

if __name__ == "__main__":
    main()
