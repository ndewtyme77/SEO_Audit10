import subprocess
import json
import tempfile

def run_lighthouse_audit(url):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    subprocess.run([
        "npx", "lighthouse", url,
        "--quiet",
        "--chrome-flags='--headless'",
        f"--output-path={tmp.name}",
        "--output=json"
    ], check=True)
    
    with open(tmp.name, "r") as f:
        return json.load(f)
