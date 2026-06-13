# 🤖 AI Resume Analyzer & Builder

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

An **AI-powered resume analyzer** built with Flask + Google Gemini AI. Upload your resume and get instant ATS scoring, skill gap analysis, job description matching, and AI-rewritten bullet points.

---

## ✨ Features

| Feature | Details |
|---|---|
| 📊 ATS Score | Overall score + breakdown (Format, Keywords, Experience, Skills) |
| 🎯 JD Match % | Compare resume against any job description |
| 🔍 Skill Gap Analysis | Skills found vs skills you should add |
| ✏️ Bullet Rewrites | AI rewrites weak bullets in STAR format |
| 💡 Action Items | 5 specific steps to improve your resume |
| 📄 Multi-format | Supports PDF, DOCX, PNG, JPG |
| 🌙 Dark UI | Clean dark-mode interface |

---

## 🗂️ Project Structure

```
ai-resume-analyzer/
├── run.py
├── requirements.txt
├── .env.example
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── main.py        # Serves frontend
│   │   └── analyze.py     # /api/analyze endpoint
│   ├── utils/
│   │   ├── extractor.py   # PDF/DOCX/image text extraction
│   │   └── gemini.py      # Gemini AI analysis logic
│   └── templates/
│       └── index.html     # Full frontend UI
```

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/tomarshaab01/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
cp .env.example .env
# Edit .env — add your GEMINI_API_KEY

# 4. Run
python run.py
# Open http://localhost:5000
```

---

## 🔑 Get Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **Create API Key**
3. Copy and paste into your `.env` file:
   ```
   GEMINI_API_KEY=your-key-here
   ```

---

## 📡 API Endpoint

**POST** `/api/analyze`

| Field | Type | Required |
|---|---|---|
| `resume` | File (PDF/DOCX/PNG/JPG) | ✅ Yes |
| `job_description` | Text | ❌ Optional |

**Response:**
```json
{
  "candidate_name": "Bharat Tomar",
  "profile_summary": "...",
  "ats_score": { "overall": 72, "breakdown": {...} },
  "strengths": [...],
  "weaknesses": [...],
  "skills_found": [...],
  "skills_missing": [...],
  "jd_match_score": 68,
  "bullet_rewrites": [...],
  "action_items": [...],
  "overall_feedback": "..."
}
```

---

## 👨‍💻 Author

**Bharat Tomar** — B.Tech AI & ML @ AKGEC-AKTU  
[LinkedIn](https://www.linkedin.com/in/bharat-tomar-026a87366) · [GitHub](https://github.com/tomarshaab01)

---

*Built as part of the AI Projects Series*
