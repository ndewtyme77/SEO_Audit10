from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from services.pagespeed import get_pagespeed_data
from services.pagerank import get_pagerank_data
from services.seo_analyzer import run_seo_analysis
from services.lighthouse import run_lighthouse_audit
from utils.pdf_generator import generate_pdf_report
from fastapi.responses import FileResponse
import tempfile

app = FastAPI(title="SEO Audit API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
async def analyze(url: str = Query(..., description="Website URL to analyze")):
    ps_data = get_pagespeed_data(url)
    pr_data = get_pagerank_data(url)
    seo_data = run_seo_analysis(url)
    lighthouse_data = run_lighthouse_audit(url)

    return {
        "pagespeed": ps_data,
        "pagerank": pr_data,
        "seo": seo_data,
        "lighthouse": lighthouse_data
    }

@app.get("/report/pdf")
async def report_pdf(url: str):
    ps_data = get_pagespeed_data(url)
    pr_data = get_pagerank_data(url)
    seo_data = run_seo_analysis(url)
    lighthouse_data = run_lighthouse_audit(url)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    generate_pdf_report(tmp.name, url, ps_data, pr_data, seo_data, lighthouse_data)
    return FileResponse(tmp.name, filename="seo_report.pdf", media_type="application/pdf")
