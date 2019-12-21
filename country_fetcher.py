import requests


def get_country(ip_address):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip_address))
        js = response.json()
        country = js['country']
        return country
    except Exception as e:
        return "Unknown"
