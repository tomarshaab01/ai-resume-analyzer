"""Gemini AI integration for resume analysis."""
import google.generativeai as genai
import json
import re


def _clean_json(raw: str) -> str:
    """Strip markdown code fences if Gemini wraps JSON in them."""
    raw = raw.strip()
    raw = re.sub(r'^```(?:json)?\s*', '', raw)
    raw = re.sub(r'\s*```$', '', raw)
    return raw.strip()


def analyze_resume(api_key: str, resume_text: str, job_description: str = '') -> dict:
    """Send resume (and optional JD) to Gemini and return structured analysis."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    jd_section = f"""
--- JOB DESCRIPTION ---
{job_description}
------------------------
""" if job_description.strip() else 'No job description provided.'

    prompt = f"""
You are an expert ATS (Applicant Tracking System) and career coach. Analyze the following resume and return a detailed JSON analysis.

RESUME TEXT:
{resume_text}

{jd_section}

Return ONLY valid JSON (no markdown, no extra text) with this exact structure:
{{
  "candidate_name": "string",
  "profile_summary": "2-3 sentence professional summary of the candidate",
  "ats_score": {{"overall": 0-100, "breakdown": {{"format": 0-25, "keywords": 0-25, "experience": 0-25, "skills": 0-25}}}},
  "strengths": ["list of 3-5 strengths"],
  "weaknesses": ["list of 3-5 areas to improve"],
  "skills_found": ["list of skills detected in resume"],
  "skills_missing": ["list of 5-8 important skills missing for the target role"],
  "jd_match_score": 0-100,
  "jd_matched_keywords": ["keywords from JD found in resume"],
  "jd_missing_keywords": ["important JD keywords missing from resume"],
  "bullet_rewrites": [
    {{"original": "original bullet from resume", "improved": "stronger STAR-format rewrite"}}
  ],
  "action_items": ["5 specific, actionable next steps to improve this resume"],
  "overall_feedback": "2-3 sentence overall verdict"
}}

Be specific, practical, and encouraging. For bullet_rewrites, pick 2-3 weakest bullets and rewrite them using strong action verbs and quantified outcomes.
"""

    response = model.generate_content(prompt)
    raw      = _clean_json(response.text)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"error": "Failed to parse AI response", "raw": response.text[:500]}
