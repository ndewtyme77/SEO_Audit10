import pdfkit
import os

WKHTML_PATH = "/usr/local/bin/wkhtmltopdf"
config = pdfkit.configuration(wkhtmltopdf=WKHTML_PATH)

def export_report_to_pdf(report_data: dict, output_path: str = "seo_report.pdf"):
    html_content = f"""
    <html><body>
    <h1>SEO Report</h1>
    <pre>{report_data}</pre>
    </body></html>
    """
    pdfkit.from_string(html_content, output_path, configuration=config)
    return output_path
