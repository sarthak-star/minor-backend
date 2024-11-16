import requests

def get_location():
    try:
        url = "http://ip-api.com/json/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            location = {
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "zip": data.get("zip"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "timezone": data.get("timezone"),
                "isp": data.get("isp")
            }
            return location
        else:
            return {"error": f"Failed to fetch location, status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}