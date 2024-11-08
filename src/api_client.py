import requests

def get_location(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    response.raise_for_status()
    data = response.json()
    return {
        "city": data["city"],
        "region": data["region"],
        "country": data["country_name"],
    }