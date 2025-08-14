from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(filename, url, ps_data, pr_data, seo_data, lighthouse_data):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 14)
    c.drawString(30, 750, f"SEO Report for {url}")
    
    c.setFont("Helvetica", 10)
    c.drawString(30, 730, f"PageSpeed Performance Score: {ps_data.get('lighthouseResult', {}).get('categories', {}).get('performance', {}).get('score', 'N/A')}")
    c.drawString(30, 715, f"Open PageRank: {pr_data.get('response', [{}])[0].get('page_rank_integer', 'N/A')}")
    c.drawString(30, 700, f"SEO Issues Found: {len(seo_data)}")
    c.drawString(30, 685, f"Lighthouse Audit Categories: {', '.join(lighthouse_data.get('categories', {}).keys())}")
    
    c.save()
