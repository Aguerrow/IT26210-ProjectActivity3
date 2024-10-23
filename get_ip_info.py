import requests

def display_ip_info():
    api_url = 'https://ipapi.co/json/'
    response = requests.get(api_url)
    response.raise_for_status()
    ip_info = response.json()

    print("Public IP Address: {}".format(ip_info['ip']))
    print("IPv6 Address: {}".format(ip_info['ipv6']))
    print("Network: {}".format(ip_info['network']))
    print("Version: {}".format(ip_info['version']))
    print("City: {}".format(ip_info['city']))
    print("Region: {}".format(ip_info['region']))
    print("Region Code: {}".format(ip_info['region_code']))
    print("Country: {}".format(ip_info['country']))
    print("Country Name: {}".format(ip_info['country_name']))
    print("Country Code: {}".format(ip_info['country_code']))
    print("Country Code ISO3: {}".format(ip_info['country_code_iso3']))
    print("Country Capital: {}".format(ip_info['country_capital']))
    print("Country TLD: {}".format(ip_info['country_tld']))
    print("Continent Code: {}".format(ip_info['continent_code']))
    print("In EU: {}".format(ip_info['in_eu']))
    print("Postal Code: {}".format(ip_info['postal']))
    print("Latitude: {}".format(ip_info['latitude']))
    print("Longitude: {}".format(ip_info['longitude']))
    print("Timezone: {}".format(ip_info['timezone']))
    print("UTC Offset: {}".format(ip_info['utc_offset']))
    print("Country Calling Code: {}".format(ip_info['country_calling_code']))
    print("Currency: {}".format(ip_info['currency']))
    print("Currency Name: {}".format(ip_info['currency_name']))
    print("Languages: {}".format(ip_info['languages']))
    print("Country Area: {}".format(ip_info['country_area']))
    print("Country Population: {}".format(ip_info['country_population']))
    print("ASN: {}".format(ip_info['asn']))
    print("Organization: {}".format(ip_info['org']))

if __name__ == "__main__":
    display_ip_info()