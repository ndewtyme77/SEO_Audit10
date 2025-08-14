import os
import requests

API_KEY = os.getenv("0wo0w4wcgwgk0gkgoo4k08048kws08cg880g8wgs")

def get_pagerank_data(url):
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    endpoint = f"https://openpagerank.com/api/v1.0/getPageRank"
    headers = {"API-OPR": API_KEY}
    params = {"domains[]": domain}
    r = requests.get(endpoint, headers=headers, params=params)
    return r.json()
