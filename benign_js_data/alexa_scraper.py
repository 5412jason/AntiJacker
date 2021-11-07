from collections import defaultdict

import requests
from bs4 import BeautifulSoup

link = "https://raw.githubusercontent.com/5412jason/AntiJacker/main/Alexa500.txt?token=AHFDXQ6LJJIATZ2ZWDY44W3BSCJFA"
data = requests.get(link)
alexa_500_list = data.text.split()

alexa_sites = []

for i in range(len(alexa_500_list))
    alexa_sites[i] = "https://www." + alexa_500_list[i]


#BASE_URL = 'https://www.alexa.com/topsites'

#print("Grabbing categories of top sites from %s".format(BASE_URL))
#resp = requests.get('https://www.alexa.com/topsites')
#soup = BeautifulSoup(resp.content, 'html.parser')

#links = soup.findAll('div', {'class': 'DescriptionCell'})
#for link in links:
    base_site_url = alexa_500_list[i].a.text.lower()
 #  site_url = "https://www." + base_site_url
 #   print(site_url)
 #   alexa_sites.append(site_url)
    try:
        page = requests.get(alexa_sites[i])
        page_soup = BeautifulSoup(page.content, "html.parser")
        json_data = page_soup.find(type="text/javascript")
        if json_data != None:
            file = open(base_site_url + ".js", 'w')
            file.write(str(json_data))
            file.close()
    except:
        print("Error parsing: %s".format(alexa_sites[i]))
