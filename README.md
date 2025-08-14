# SEO Optimization Web App

A full-stack SEO audit tool using **FastAPI** backend and **React** frontend.

## Features
- Core Web Vitals from Google PageSpeed API
- Keyword extraction from SERPs (BeautifulSoup)
- Backlinks from Open PageRank API
- Technical SEO audit (python-seo-analyzer)
- Visual charts (Chart.js)
- PDF export

## Deployment
- Backend → Render (free tier)
- Frontend → Vercel (free tier)

## Directory Structure
- `backend/` → API code
- `frontend/` → Web interface

## Local Development
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm start
