from bs4 import BeautifulSoup, Tag
import requests
import re

def header():
    return  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'close'
    }


def climate(city, country):

    country_only =  [ 'yerevan','baku','manama','bujumbura','phnom penh','djibouti','santo domingo','san salvador','tbilisi','guatemala city','port au prince','hong kong','tehran','baghdad','tel aviv','kingston',
        'astana','kuwait city','beirut','monrovia','macao','lilongwe','kuala lumpur','ulaanbaatar','kathmandu','auckland','managua','muscat','panama city','manila','san juan','doha','riyadh','freetown','singapore',
        'taibei','port of spain','tashkent','ho chi minh city','hanoi','lusaka'  ]

    country = country.replace(' ', '-')
    city = city.replace(' ', '-')
    insert = country + '/' + city

    if city in country_only:
        insert = country

    headers = header()
    response = requests.get('https://www.climatestotravel.com/climate/' + insert, headers=headers, timeout=8)

    try:
        response.raise_for_status()
    except Exception as exc:
        print('there was a problem: %s' % (exc))

    soup = BeautifulSoup(response.text, 'html.parser')

    data_list = []

    # temperature
    temp_table = soup.find('tr', "min-table").parent
    for month in temp_table.find_all('th', scope="row"):
        for temp in month.parent.find_all('td', limit=2):
            data_list.append(temp.get_text())

    # precipitation
    x = 4
    precipit_table = soup.find('tr', "precipit-table").parent
    for month in precipit_table.find_all('th', scope="row"):
        for precipit in month.parent.find_all('td'):
            if x % 3 == 0 or x % 3 == 1:                                          # modulo to get only the first and third data element
                data_list.append(precipit.get_text())
            x += 1

    # sunshine
    sun_data = []
    table = soup.find('table', class_="sole")
    for child in table.children:
        if isinstance(child, Tag):
            sun_data.append(child.get_text())
    for x in range(4, 40, 3):
        data_list.append(sun_data[x])

    return data_list



def expat(city, country):

    city = city.replace(' ', '-')
    headers = header()
    response = requests.get('https://www.expatistan.com/cost-of-living/' + city + '?currency=USD', headers=headers,
                            timeout=5)

    try:
        response.raise_for_status()
    except Exception as exc:
        print('there was a problem: %s' % (exc))

    soup = BeautifulSoup(response.text, 'html.parser')

    lunch = soup.find('a', text='Basic lunchtime menu (including a drink) in the business district')
    movies = soup.find('a', text='2 tickets to the movies')
    beer = soup.find('a', text='1 beer in neighbourhood pub (500ml or 1pt.) ')
    rent = soup.find('a', text='Monthly rent for 85 m2 (900 sqft) furnished accommodation in normal area')
    utilities = soup.find('a', text='Utilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat')
    microwave = soup.find('a', text='Microwave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)')
    cleaning = soup.find('a', text='Hourly rate for cleaning help')
    gas = soup.find('a', text='1 liter (1/4 gallon) of gas')
    transport = soup.find('a', text='Monthly ticket public transport')
    jeans = soup.find('a', text='1 pair of jeans (levis 501 or similar)')
    shoes = soup.find('a', text='1 pair of sport shoes (nike, adidas, or equivalent brands)')
    chicken = soup.find('a', text='500 gr (1 lb.) of boneless chicken breast')
    wine = soup.find('a', text='1 bottle of red table wine, good quality')
    cola = soup.find('a', text='2 liters of coca-cola')

    data_elements = [lunch, movies, beer, rent, utilities, microwave, cleaning, gas, transport, jeans, shoes, chicken,
                     wine, cola]

    regex = r'\(\$(\d+.?\d*)\)'
    regex2 = r'.+\$(\d+.?\d*)'
    usd = ''
    data_list = []

    for element in data_elements:
        x = 0
        for sibling in element.parent.next_siblings:
            if country != 'United States':
                x += 1  # should run 4 times
                try:
                    usd = sibling.find('i')
                    usd = usd.get_text()
                    usd = re.search(regex, usd)
                    data = usd.group(1)
                    data_list.append(data.replace(',', ''))
                except:
                    continue
            if country == 'United States':
                x += 1.4  # must run 3 times
                try:
                    if len(sibling.get_text()) > 2:  # get rid of '\n'
                        usd = sibling.get_text()
                        usd = re.search(regex2, usd)
                        data = usd.group(1)
                        data_list.append(data.replace(',', ''))
                except:
                    continue
            if x >= 4: break

    return data_list


def numbeo_crime(city):

    city = city.replace(' ', '-')
    headers = header()
    response = requests.get('https://www.numbeo.com/crime/in/' + city, headers=headers, timeout=5)

    try:
        response.raise_for_status()
    except Exception as exc:
        print('there was a problem: %s' % (exc))

    soup = BeautifulSoup(response.text, 'html.parser')

    level_crime = soup.find('td', text="Level of crime")
    home_broken = soup.find('td', text="Worries home broken and things stolen")
    mugged_robbed = soup.find('td', text="Worries being mugged or robbed")
    car_stolen = soup.find('td', text="Worries car stolen")
    attacked = soup.find('td', text="Worries attacked")
    insulted = soup.find('td', text="Worries being insulted")
    drugs = soup.find('td', text="Problem people using or dealing drugs")
    level_safety_walk_day = soup.find('td', text="Safety walking alone during daylight")
    level_safety_walk_night = soup.find('td', text="Safety walking alone during night")

    scrape_list = [level_crime, home_broken,
                   mugged_robbed, car_stolen, attacked, insulted,
                   drugs, level_safety_walk_day, level_safety_walk_night]

    data_list = []
    regex = r'(\d+.?\d*)'

    for item in scrape_list:
        for line in item.next_siblings:
            if isinstance(line, Tag):  # get rid of empty lines which are NavigableStrings
                if len(line.get_text()) > 2:  # get rid of tags without text content or blancs
                    data = line.get_text()
                    data = re.search(regex, data)
                    data = data.group(1)
                    data_list.append(data)

    return  data_list


def numbeo_pollution(city):

    city = city.replace(' ', '-')
    headers = header()
    response = requests.get('https://www.numbeo.com/pollution/in/' + city, headers=headers, timeout=5)

    try:
        response.raise_for_status()
    except Exception as exc:
        print('there was a problem: %s' % (exc))

    soup = BeautifulSoup(response.text, 'html.parser')

    pollution_index = soup.find('td', text="Pollution Index: ")
    air_pollution = soup.find('td', text="Air Pollution")
    drinking_water_pollution = soup.find('td', text="Drinking Water Pollution and Inaccessibility")
    dirty_untidy = soup.find('td', text="Dirty and Untidy")
    noise_pollution = soup.find('td', text="Noise and Light Pollution")
    water_pollution = soup.find('td', text="Water Pollution")
    comfortable_time_spend_city = soup.find('td', text="Comfortable to Spend Time in the City")
    quality_green_parks = soup.find('td', text="Quality of Green and Parks")

    scrape_list = [pollution_index, air_pollution, drinking_water_pollution, dirty_untidy,
                   noise_pollution, water_pollution,
                   comfortable_time_spend_city, quality_green_parks]

    data_list = []
    regex = r'(\d+.?\d*)'

    for item in scrape_list:
        for line in item.next_siblings:
            if isinstance(line, Tag):  # get rid of empty lines which are NavigableStrings
                if len(line.get_text()) > 2:  # get rid of tags without text content or blancs
                    data = line.get_text()
                    data = re.search(regex, data)
                    data = data.group(1)
                    data_list.append(data)

    return data_list
