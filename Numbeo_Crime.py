from bs4 import Tag, NavigableString, BeautifulSoup
import requests

# changes to be made for USD prices if country is USA
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

crime_index = soup.find('th', text='Index').parent.parent
list = crime_index.find_all('td')
print(f' Crime index in {city}, {country} = {list[1].get_text()}\n')

level_crime = soup.find('td', text="Level of crime")
home_broken = soup.find('td', text="Worries home broken and things stolen")
mugged_robbed = soup.find('td', text="Worries being mugged or robbed")
car_stolen = soup.find('td', text="Worries car stolen")

scrape_list = [level_crime, home_broken, mugged_robbed, car_stolen]

for element in scrape_list:
    print(element.get_text())
    for line in element.next_siblings:
        if isinstance(line, Tag):                      # get rid of empty lines which are NavigableStrings
            if len(line.get_text()) > 2:               # get rid of tags without text content or blancs
                print(line.get_text())
    print()



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


# daar kan je een .get_text() methode op loslaten
# for line in soup.find('h2').next_siblings:
#     print(line.get_text())
# OUTPUT :  (partial)
#
#
# Level
# of
# crime89
# .34
# Very
# High
# Crime
# increasing in the
# past
# 3
# years81
# .02
# Very
# High
# Worries
# home
# broken and things
# stolen78
# .97
# High
# Worries
# being
# mugged or robbed81
# .33
# Very
# High
# Worries
# car
# stolen77
# .57
# High
# Worries
# things
# from car stolen81
#
# .21
# Very
# High
# Worries
# attacked75
# .41
# High
# Worries
# being
# insulted63
# .18
# High
# Worries
# being
# subject
# to
# a
# physical
# attack
# because
# of
# your
# skin
# color, ethnic
# origin, gender or religion65
# .78
# High
# Problem
# people
# using or dealing
# drugs71
# .43
# High
# Problem
# property
# crimes
# such as vandalism and theft82
# .68
# Very
# High
# Problem
# violent
# crimes
# such as assault and armed
# robbery88
# .34
# Very
# High
# Problem
# corruption and bribery91
# .94
# Very
# High
#
# whenDocReady(function()
# {
# $(function() {
# $( "#level_of_crime").progressbar({
#     value: 89.34
# });
# $("#crime_increasing").progressbar({
#     value: 81.02
# });
# $("#worried_home_broken").progressbar({
#     value: 78.97
# });
# $("#worried_mugged_robbed").progressbar({
#     value: 81.33
# });
# $("#worried_car_stolen").progressbar({
#     value: 77.57
# });
# $("#worried_things_car_stolen").progressbar({
#     value: 81.21
# });
# $("#worried_attacked").progressbar({
#     value: 75.41
# });
# $("#worried_insulted").progressbar({
#     value: 63.18

