from collections import defaultdict

import requests
from bs4 import BeautifulSoup

alexa_sites = []
BASE_URL = 'https://www.alexa.com/topsites'

print("Grabbing categories of top sites from %s".format(BASE_URL))
resp = requests.get('https://www.alexa.com/topsites')
soup = BeautifulSoup(resp.content, 'html.parser')

links = soup.findAll('div', {'class': 'DescriptionCell'})
for link in links:
    base_site_url = link.a.text.lower()
    site_url = "https://www." + base_site_url
    print(site_url)
    alexa_sites.append(site_url)
    try:
        page = requests.get(site_url)
        page_soup = BeautifulSoup(page.content, "html.parser")
        json_data = page_soup.find(type="text/javascript")
        if json_data != None:
            file = open(base_site_url + ".js", 'w')
            file.write(str(json_data))
            file.close()
    except:
        print("Error parsing: %s".format(site_url))
