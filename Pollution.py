from bs4 import Tag, NavigableString, BeautifulSoup
import requests

country = 'Belgium'
city = "city2_values"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'}
response = requests.get('https://www.numbeo.com/pollution/in/' + city, headers=headers, timeout=5)

try:
    response.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

soup = BeautifulSoup(response.text, 'html.parser')

pollution_index = soup.find('td', text="Pollution Index: ")
air_pollution = soup.find('td', text="Air Pollution")
drinking_water_quality = soup.find('td', text="Drinking Water Quality and Accessibility")
dirty_untidy = soup.find('td', text="Dirty and Untidy")
noise_pollution = soup.find('td', text="Noise and Light Pollution")
water_pollution = soup.find('td', text="Water Pollution")
comfortable_time_spend_city = soup.find('td', text= "Comfortable to Spend Time in the City")
quality_green_parks = soup.find('td', text="Quality of Green and Parks")

scrape_list = [pollution_index, air_pollution, drinking_water_quality, dirty_untidy, noise_pollution, noise_pollution, water_pollution,
               comfortable_time_spend_city, quality_green_parks]

for item in scrape_list:
    print(item.get_text())
    for line in item.next_siblings:
        if isinstance(line, Tag):                      # get rid of empty lines which are NavigableStrings
            if len(line.get_text()) > 2:               # get rid of tags without text content or blancs
                print(line.get_text())
    print()
