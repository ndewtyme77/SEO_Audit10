#from seoanalyzer import analyze
from seo_analyzer import analyze

def run_seo_analysis(url):
    results = analyze(url, analyze_headings=True, analyze_keywords=True, analyze_description=True)
    return results
