import requests

def search(drug):
    response = requests.get("https://api.fda.gov/drug/event.json?limit=1")
    print(response.text)
search('tylenol')
