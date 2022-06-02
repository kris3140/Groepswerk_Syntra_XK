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


for item in scrape_list:
    print(item.get_text())
    for line in item.next_siblings:
        if isinstance(line, Tag):                      # get rid of empty lines which are NavigableStrings
            if len(line.get_text()) > 2:               # get rid of tags without text content or blancs
                print(line.get_text())
    print()




# crime_index = soup.find('td', text="Crime Index: ")
# print(crime_index.string, end='')
# for line in crime_index.next_siblings:
#     if isinstance(line, Tag):
#         if len(line.get_text()) > 3:
#             print(line.get_text())
# print()
# print(soup.prettify())
# row 544 = crime index

#
# crime_index = soup.find('th', text='Index').parent.parent
# index = crime_index.find_all('td')
# print(index)
# OUTPUT:
# [<td>Crime Index: </td>,
# <td style="text-align: right">80.49</td>,
# <td>Safety Index: </td>,
# <td style="text-align: right">19.51</td>]


# dit genereert 1 lijn, met de eerste die het vindt
# header2 = soup.find('h2')
# print(header2)
# OUTPUT:
# <h2>Crime rates in Johannesburg, South Africa</h2>

# find_all genereert een lijst
# header2 = soup.find('h2')
# print(header2)
# OUTPUT: (blijkbaar zijn er 2)
# [<h2>Crime rates in Johannesburg, South Africa</h2>, <h2>Safety in Johannesburg, South Africa</h2>]

# find met een methode .descendants,... genereert een object
# header2 = soup.find('h2').descendants
# print(header2)
# OUTPUT: een object
# <generator object Tag.descendants at 0x000001F74DE0EC10>
# dit object kan je met een loop doorlopen
# for line in soup.find('h2').next_siblings:
#     print(line)
# line is dan een Tag object, maar ook NavigableString objecten (check met print(type(line))
# output : <class 'bs4.element.NavigableString'> of <class 'bs4.element.Tag'>
# de blanco lijnen zijn NavigableString en zorgen ervoor dat je vastloopt met je tag methods zoals .get_text()
# OUTPUT:
#
# <table class="table_builder_with_value_explanation data_wide_table">
# <tr>
# <td class="columnWithName">Level of crime</td>
# <td><div class="jquery_bar" id="level_of_crime"></div></td>
# <td class="indexValueTd" style="text-align: right">89.34
# <td class="hidden_on_small_mobile"><span class="red_standard"># Very High</span></td></td></tr>
# <tr><td class="columnWithName">Crime increasing in the past 3 years</td><td><div class="jquery_bar" id="crime_increasing"></div></td><td class="indexValueTd" style="text-align: right">81.02<td class="hidden_on_small_mobile"><span class="red_standard">
# Very High</span></td></td></tr>
# <tr><td class="columnWithName">Worries home broken and things stolen</td><td><div class="jquery_bar" id="worried_home_broken"></div></td><td class="indexValueTd" style="text-align: right">78.97<td class="hidden_on_small_mobile"><span class="red_light_standard">
# High</span></td></td></tr>
# <tr><td class="columnWithName">Worries being mugged or robbed</td><td><div class="jquery_bar" id="worried_mugged_robbed"></div></td><td class="indexValueTd" style="text-align: right">81.33<td class="hidden_on_small_mobile"><span class="red_standard">
# Very High</span></td></td></tr>

