import os
import requests

API_KEY = os.getenv("AIzaSyDYVScIAM7Inox1Rp6EN8__a6l3U_pfJcg")

def get_pagespeed_data(url):
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {"url": url, "key": API_KEY, "strategy": "desktop"}
    r = requests.get(endpoint, params=params)
    return r.json()
