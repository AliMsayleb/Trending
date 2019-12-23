import requests


def get_country_code(ip_address):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip_address))
        js = response.json()
        country = js['countryCode']
        return country
    except Exception as e:
        return "WW"


def get_country_id(country_code):
    import countries_woeid
    if country_code in countries_woeid.countries_woeid:
        return countries_woeid.countries_woeid[country_code]['woeid']
    else:
        return 1


def get_country_name(country_code):
    import countries_woeid
    if country_code in countries_woeid.countries_woeid:
        return countries_woeid.countries_woeid[country_code]['country']
    else:
        return "WorldWide"
