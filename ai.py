from google import genai 
from google.genai import types
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client()


def analyze_resume(resume_text, user_goal):
    prompt =f"""
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools [excel for backend, etc]
- Identify real gaps
- Generate roadmap only for missing fields
- Make output DIFFIERENT based on goal

Return only JSON:
{{
"skills":[],
"missing_skills": [],
"roadmap":[],
"interview_question": []

}}

Resume:
{resume_text}

"""
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a strict hiring manager.",
                temperature=0.3,
                response_mime_type="application/json",
            ),
        )

        return json.loads(response.text)
        
    except Exception as e:
        return {
            "skills":[],
            "missing_skills": [],
            "roadmap":[],
            "interview_question": [],
            "error": str(e)
        }
