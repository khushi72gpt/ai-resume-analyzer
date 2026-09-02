# 🚀 AI Resume Analyzer

An intelligent, AI-powered web application that analyzes resumes against job descriptions, provides detailed compatibility, highlights key strengths, identifies skill gaps, and suggests actionable improvements using **Google Gemini AI** and **TiDB Cloud**.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![TiDB Cloud](https://img.shields.io/badge/TiDB%20Cloud-MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)

---

## ✨ Features

- **Automated Parsing**: Parses PDF and DOCX resume files seamlessly.
- **AI-Powered Analysis**: Leverages Google Gemini AI to evaluate resumes against target job roles.
- **Match Score & Feedback**: Provides an overall compatibility score, key strengths, missing skills, and formatting recommendations.
- **Database Storage**: Stores user submissions and analysis history securely using SQLAlchemy and TiDB Cloud.
- **Cloud Ready**: Deployed live on Render with robust environment configuration.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy
- **Database**: TiDB Cloud (MySQL compatible) with PyMySQL & Certifi SSL
- **AI Engine**: Google Generative AI (Gemini API)
- **Document Processors**: PyPDF2, python-docx
- **Deployment**: Render (Gunicorn WSGI)

---

## 📁 Project Structure

```text
ai-resume-analyzer/
├── app.py              # Main Flask application & routes
├── db.py               # Database configuration & SQLAlchemy setup
├── requirements.txt    # Cleaned project dependencies
├── .env                # Local environment variables (git-ignored)
├── .gitignore          # Ignored files (secrets, venv, cache)
├── templates/          # HTML templates
│   ├── index.html      # Upload & Form page
│   └── result.html     # Resume evaluation results page
└── static/             # Static assets (CSS, JS, Images)
