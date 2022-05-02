from bs4 import Tag, NavigableString, BeautifulSoup
import requests

country = 'south-africa'
city = "Johannesburg"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}
response = requests.get('https://www.numbeo.com/crime/in/' + city, headers=headers, timeout=5)

try:
    response.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

soup = BeautifulSoup(response.text, 'html.parser')

crime_index = soup.find('td', text="Crime Index: ")
safety_index = soup.find('td', text="Safety Index: ")
level_crime = soup.find('td', text="Level of crime")
home_broken = soup.find('td', text="Worries home broken and things stolen")
mugged_robbed = soup.find('td', text="Worries being mugged or robbed")
car_stolen = soup.find('td', text="Worries car stolen")
attacked = soup.find('td', text="Worries attacked")
insulted = soup.find('td', text="Worries being insulted")
drugs = soup.find('td', text="Problem people using or dealing drugs")
level_safety_walk_day = soup.find('td', text="Safety walking alone during daylight")
level_safety_walk_night = soup.find('td', text="Safety walking alone during night")

