import requests

def get_ip_info(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def display_ip_info():
    ipv4_url = 'https://api.ipify.org?format=json'
    ipapi_url = 'https://ipapi.co/json/'

    ipv4_info = get_ip_info(ipv4_url)
    ipapi_info = get_ip_info(ipapi_url)

    print("IPv4 Address: {}".format(ipv4_info.get('ip')))
    print("IPv6 Address: {}".format(ipapi_info.get('ip')))
    print("Network: {}".format(ipapi_info['network']))
    print("Version: {}".format(ipapi_info['version']))
    print("City: {}".format(ipapi_info['city']))
    print("Region: {}".format(ipapi_info['region']))
    print("Region Code: {}".format(ipapi_info['region_code']))
    print("Country: {}".format(ipapi_info['country']))
    print("Country Name: {}".format(ipapi_info['country_name']))
    print("Country Code: {}".format(ipapi_info['country_code']))
    print("Country Code ISO3: {}".format(ipapi_info['country_code_iso3']))
    print("Country Capital: {}".format(ipapi_info['country_capital']))
    print("Country TLD: {}".format(ipapi_info['country_tld']))
    print("Continent Code: {}".format(ipapi_info['continent_code']))
    print("In EU: {}".format(ipapi_info['in_eu']))
    print("Postal Code: {}".format(ipapi_info['postal']))
    print("Latitude: {}".format(ipapi_info['latitude']))
    print("Longitude: {}".format(ipapi_info['longitude']))
    print("Timezone: {}".format(ipapi_info['timezone']))
    print("UTC Offset: {}".format(ipapi_info['utc_offset']))
    print("Country Calling Code: {}".format(ipapi_info['country_calling_code']))
    print("Currency: {}".format(ipapi_info['currency']))
    print("Currency Name: {}".format(ipapi_info['currency_name']))
    print("Languages: {}".format(ipapi_info['languages']))
    print("Country Area: {}".format(ipapi_info['country_area']))
    print("Country Population: {}".format(ipapi_info['country_population']))
    print("ASN: {}".format(ipapi_info['asn']))
    print("Organization: {}".format(ipapi_info['org']))

if __name__ == "__main__":
    display_ip_info()