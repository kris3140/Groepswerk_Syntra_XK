from bs4 import BeautifulSoup
import requests


country = "belgium"
city = "brussels"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}

response = requests.get('https://www.weather-atlas.com/en/' + country + '/' + city + '-climate', headers=headers, timeout=5)

try:
    response.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

soup = BeautifulSoup(response.text, 'html.parser')


print("Average sunshine: ")
tabel = soup.find("a", text="Average sunshine in January").parent.parent
print(tabel.find('li').span.get_text()[:-1])
for line in tabel.find("li").next_siblings:
    print(line.span.get_text()[:-1])

tabel2 = soup.find("a", text="Average sunshine in July").parent.parent
print(tabel2.find('li').span.get_text()[:-1])
for line in tabel2.find("li").next_siblings:
    print(line.span.get_text()[:-1])

print("Average humidity: ")
tabel = soup.find("a", text="Average humidity in January").parent.parent
print(tabel.find('li').span.get_text()[:-1])
for line in tabel.find("li").next_siblings:
    print(line.span.get_text()[:-1])

tabel2 = soup.find("a", text="Average humidity in July").parent.parent
print(tabel2.find('li').span.get_text()[:-1])
for line in tabel2.find("li").next_siblings:
    print(line.span.get_text()[:-1])





# tabel = soup.find("a", text="Average sunshine in January").parent.parent
# tabel2 = soup.find("a", text="Average sunshine in July").parent.parent
# <ul class="list-unstyled mb-0"><li><a href="/en/india/mumbai-weather-january#daylight_sunshine" title="Climate data
# - January">Average sunshine in January</a>: <br class="br-xs"/><span class="fw-bold">8.7h
# </span></li><li><a href="/en/india/mumbai-weather-february#daylight_sunshine" title="Climate data
# - February">Average sunshine in February</a>: <br class="br-xs"/><span class="fw-bold">9.2
# </span></li><li><a href="/en/india/mumbai-weather-march#daylight_sunshine" title="Climate data
# - March">Average sunshine in March</a>: <br class="br-xs"/><span class="fw-bold">8.8h</span></li><li><a href="/en/india/mumbai-weather-april#daylight_sunshine" title="Climate data - April">Average sunshine in April</a>: <br class="br-xs"/><span class="fw-bold">9.5h</span></li><li><a href="/en/india/mumbai-weather-may#daylight_sunshine" title="Climate data - May">Average sunshine in May</a>: <br class="br-xs"/><span class="fw-bold">9.6h</span></li><li><a href="/en/india/mumbai-weather-june#daylight_sunshine" title="Climate data - June">Average sunshine in June</a>: <br class="br-xs"/><span class="fw-bold">5h</span></li></ul>

# <ul class="list-unstyled mb-0"><li><a href="/en/india/mumbai-weather-july#daylight_sunshine" title="Climate data - July">Average sunshine in July</a>: <br class="br-xs"/><span class="fw-bold">2.4h</span></li><li><a href="/en/india/mumbai-weather-august#daylight_sunshine" title="Climate data - August">Average sunshine in August</a>: <br class="br-xs"/><span class="fw-bold">2.4h</span></li><li><a href="/en/india/mumbai-weather-september#daylight_sunshine" title="Climate data - September">Average sunshine in September</a>: <br class="br-xs"/><span class="fw-bold">5.5h</span></li><li><a href="/en/india/mumbai-weather-october#daylight_sunshine" title="Climate data - October">Average sunshine in October</a>: <br class="br-xs"/><span class="fw-bold">7.7h</span></li><li><a href="/en/india/mumbai-weather-november#daylight_sunshine" title="Climate data - November">Average sunshine in November</a>: <br class="br-xs"/><span class="fw-bold">8.2h</span></li><li><a href="/en/india/mumbai-weather-december#daylight_sunshine" title="Climate data - December">Average sunshine in December</a>: <br class="br-xs"/><span class="fw-bold">8.2h</span></li></ul>

# one line = from <li> to </li>
#  <li><a href="/en/india/mumbai-weather-april#daylight_sunshine" title="Climate data - April">Average sunshine in April</a>
#  : <br class="br-xs"/><span class="fw-bold">9.5h</span></li>

