from bs4 import BeautifulSoup
import requests
import re

country = 'japan'
city = "tokyo"

# country = 'china'
# city = "shanghai"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}

response = requests.get('https://www.expatistan.com/cost-of-living/' + city +'?currency=USD', headers=headers, timeout=5)

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

data_elements = [lunch, movies, beer, rent, utilities, microwave, cleaning, gas, transport, jeans, shoes, chicken, wine, cola]

regex = r'\(\$(\d+.?\d*)\)'
regex2 = r'.+\$(\d+.?\d*)'
usd = ''


print(f'{country} / {city}: ')
for element in data_elements:
    x = 0
    for sibling in element.parent.next_siblings:
        if country != 'united states':
            x += 1                                               # should run 4 times
            try:
                usd = sibling.find('i')
                usd = usd.get_text()
                usd = re.search(regex, usd)
                data = usd.group(1)
                print(country, ";" ,city,";" ,element.get_text(), '; ', data.replace(',', ''))
            except:
                continue
        if country == 'united states':
            x += 1.4                                          # must run 3 times
            try:
                if len(sibling.get_text()) > 2:               # get rid of '\n'
                    usd = sibling.get_text()
                    usd = re.search(regex2, usd)
                    data = usd.group(1)
                    print(country, ";" ,city,";", element.get_text(), '; ', data.replace(',', ''))
            except:
                continue
        if x >= 4: break




# structuur
# tr
#     td leeg
#     td
#         a (met tekst)
#     td (euro)
#     td
#         i (usd)
# tr is never closed, so you keep getting everything when you ask for a child of TR
# and when you do parent.parent you go all the way up to the first TR and also then you get everything again
# with parent.next_siblings you go up from a to td and then the next td's, search for an i and limit the search to 4 tags





    # print(soup.prettify())
# row 294 :  Family of four estimated monthly costs
# row 1065 : Basic lunchtime menu (including a drink) in the business district

# this gives you all the items + cost in EUR + cost in USD with a lot of blanc lines in between
# lunch = soup.find('a', text='Basic lunchtime menu (including a drink) in the business district')
# print(lunch.get_text())
# for line in soup.find('a', text='Basic lunchtime menu (including a drink) in the business district').parent.next_siblings:
#     print(line.get_text())

# lunch = soup.find('a', text='Basic lunchtime menu (including a drink) in the business district')
# print(lunch.get_text())
# x = 0
# for line in lunch.parent.next_siblings:
#     x += 1
#     try:
#         usd = line.find('i')
#         print(usd.get_text())
#     except:
#         continue
#     if x == 4: break
#  output :
# Basic lunchtime menu (including a drink) in the business district
# ($19)

#
# if country == 'usa':
#     try:
#         datalist.append(sibling.get_text())
#     except:
#         continue
# Basic lunchtime menu (including a drink) in the business district
# ['\n', '\n                  \n                      $19\n                  \n                ', '\n', "\n\n\nCombo meal in fast food restaurant (big mac meal or similar)\n\n\n                  \n                      $10\n                  \n                \n\n\n\n500 gr (1 lb.) of boneless chicken breast\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 liter (1 qt.) of whole fat milk\n\n\n                  \n                      $1.28\n                  \n                \n\n\n\n12 eggs, large\n\n\n                  \n                      $4.52\n                  \n                \n\n\n\n1 kg (2 lb.) of tomatoes\n\n\n                  \n                      $4.60\n                  \n                \n\n\n\n500 gr (16 oz.) of local cheese\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 kg (2 lb.) of apples\n\n\n                  \n                      $3.52\n                  \n                \n\n\n\n1 kg (2 lb.) of potatoes\n\n\n                  \n                      $1.91\n                  \n                \n\n\n\n0.5 l (16 oz) domestic beer in the supermarket\n\n\n                  \n                      $4.23\n                  \n                \n\n\n\n1 bottle of red table wine, good quality\n\n\n                  \n                      $19\n                  \n                \n\n\n\n2 liters of coca-cola\n\n\n                  \n                      $2.53\n                  \n                \n\n\n\nBread for 2 people for 1 day\n\n\n                  \n                      $3.29\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nHousing\n\nUpdate prices\n\n\n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in expensive area\n\n\n                  \n                      $5,461\n                  \n                \n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in normal area\n\n\n                  \n                      $3,543\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat\n\n\n                  \n                      $164\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in expensive area\n\n\n                  \n                      $3,516\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in normal area\n\n\n                  \n                      $2,334\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 1 person in 45 m2 (480 sqft) studio\n\n\n                  \n                      $126\n                  \n                \n\n\n\nInternet 8 mbps (1 month)\n\n\n                  \n                      $61\n                  \n                \n\n\n\n40” flat screen tv\n\n\n                  \n                      $320\n                  \n                \n\n\n\nMicrowave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)\n\n\n                  \n                      $182\n                  \n                \n\n\n\nLaundry detergent (3 l. ~ 100 oz.)\n\n\n                  \n                      $12\n                  \n                \n\n\n\nHourly rate for cleaning help\n\n\n                  \n                      $30\n                  \n                \n\n\n\n\n\n\n\nClothes\n\nUpdate prices\n\n\n\n\n\n1 pair of jeans (levis 501 or similar)\n\n\n                  \n                      $59\n                  \n                \n\n\n\n1 summer dress in a high street store (zara, h&m or similar retailers)\n\n\n                  \n                      $42\n                  \n                \n\n\n\n1 pair of sport shoes (nike, adidas, or equivalent brands)\n\n\n                  \n                      $92\n                  \n                \n\n\n\n1 pair of men’s leather business shoes\n\n\n                  \n                      $123\n                  \n                \n\nTransportation\n\nUpdate prices\n\n\n\n\n\nVolkswagen golf 1.4 tsi 150 cv (or equivalent), with no extras, new\n\n\n                  \n                      $22,801\n                  \n                \n\n\n\n1 liter (1/4 gallon) of gas\n\n\n                  \n                      $1.02\n                  \n                \n\n\n\nMonthly ticket public transport\n\n\n                  \n                      $128\n                  \n                \n\n\n\nTaxi trip on a business day, basic tariff, 8 km. (5 miles)\n\n\n                  \n                      $31\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nPersonal Care\n\nUpdate prices\n\n\n\n\n\nCold medicine for 6 days (tylenol, frenadol, coldrex, or equivalent brands)\n\n\n                  \n                      $7\n                  \n                \n\n\n\n1 box of antibiotics (12 doses)\n\n\n                  \n                      $24\n                  \n                \n\n\n\nShort visit to private doctor (15 minutes)\n\n\n                  \n                      $163\n                  \n                \n\n\n\n1 box of 32 tampons (tampax, ob, ...)\n\n\n                  \n                      $8\n                  \n                \n\n\n\nDeodorant, roll-on (50ml ~ 1.5 oz.)\n\n\n                  \n                      $4.61\n                  \n                \n\n\n\nHair shampoo 2-in-1 (400 ml ~ 12 oz.)\n\n\n                  \n                      $8\n                  \n                \n\n\n\n4 rolls of toilet paper\n\n\n                  \n                      $4.81\n                  \n                \n\n\n\nTube of toothpaste\n\n\n                  \n                      $2.11\n                  \n                \n\n\n\nStandard men's haircut in expat area of the city\n\n\n                  \n                      $30\n                  \n                \n\nEntertainment\n\nUpdate prices\n\n\n\n\n\nBasic dinner out for two in neighborhood pub\n\n\n                  \n                      $63\n                  \n                \n\n\n\n2 tickets to the movies\n\n\n                  \n                      $32\n                  \n                \n\n\n\n2 tickets to the theater (best available seats)\n\n\n                  \n                      $397\n                  \n                \n\n\n\nDinner for two at an italian restaurant in the expat area including appetisers, main course, wine and dessert\n\n\n                  \n                      $114\n                  \n                \n\n\n\n1 cocktail drink in downtown club\n\n\n                  \n                      $16\n                  \n                \n\n\n\nCappuccino in expat area of the city\n\n\n                  \n                      $5.12\n                  \n                \n\n\n\n1 beer in neighbourhood pub (500ml or 1pt.) \n\n\n                  \n                      $7\n                  \n                \n\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n"]
# 2 tickets to the movies
# ['\n', '\n                  \n                      $19\n                  \n                ', '\n', "\n\n\nCombo meal in fast food restaurant (big mac meal or similar)\n\n\n                  \n                      $10\n                  \n                \n\n\n\n500 gr (1 lb.) of boneless chicken breast\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 liter (1 qt.) of whole fat milk\n\n\n                  \n                      $1.28\n                  \n                \n\n\n\n12 eggs, large\n\n\n                  \n                      $4.52\n                  \n                \n\n\n\n1 kg (2 lb.) of tomatoes\n\n\n                  \n                      $4.60\n                  \n                \n\n\n\n500 gr (16 oz.) of local cheese\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 kg (2 lb.) of apples\n\n\n                  \n                      $3.52\n                  \n                \n\n\n\n1 kg (2 lb.) of potatoes\n\n\n                  \n                      $1.91\n                  \n                \n\n\n\n0.5 l (16 oz) domestic beer in the supermarket\n\n\n                  \n                      $4.23\n                  \n                \n\n\n\n1 bottle of red table wine, good quality\n\n\n                  \n                      $19\n                  \n                \n\n\n\n2 liters of coca-cola\n\n\n                  \n                      $2.53\n                  \n                \n\n\n\nBread for 2 people for 1 day\n\n\n                  \n                      $3.29\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nHousing\n\nUpdate prices\n\n\n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in expensive area\n\n\n                  \n                      $5,461\n                  \n                \n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in normal area\n\n\n                  \n                      $3,543\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat\n\n\n                  \n                      $164\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in expensive area\n\n\n                  \n                      $3,516\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in normal area\n\n\n                  \n                      $2,334\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 1 person in 45 m2 (480 sqft) studio\n\n\n                  \n                      $126\n                  \n                \n\n\n\nInternet 8 mbps (1 month)\n\n\n                  \n                      $61\n                  \n                \n\n\n\n40” flat screen tv\n\n\n                  \n                      $320\n                  \n                \n\n\n\nMicrowave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)\n\n\n                  \n                      $182\n                  \n                \n\n\n\nLaundry detergent (3 l. ~ 100 oz.)\n\n\n                  \n                      $12\n                  \n                \n\n\n\nHourly rate for cleaning help\n\n\n                  \n                      $30\n                  \n                \n\n\n\n\n\n\n\nClothes\n\nUpdate prices\n\n\n\n\n\n1 pair of jeans (levis 501 or similar)\n\n\n                  \n                      $59\n                  \n                \n\n\n\n1 summer dress in a high street store (zara, h&m or similar retailers)\n\n\n                  \n                      $42\n                  \n                \n\n\n\n1 pair of sport shoes (nike, adidas, or equivalent brands)\n\n\n                  \n                      $92\n                  \n                \n\n\n\n1 pair of men’s leather business shoes\n\n\n                  \n                      $123\n                  \n                \n\nTransportation\n\nUpdate prices\n\n\n\n\n\nVolkswagen golf 1.4 tsi 150 cv (or equivalent), with no extras, new\n\n\n                  \n                      $22,801\n                  \n                \n\n\n\n1 liter (1/4 gallon) of gas\n\n\n                  \n                      $1.02\n                  \n                \n\n\n\nMonthly ticket public transport\n\n\n                  \n                      $128\n                  \n                \n\n\n\nTaxi trip on a business day, basic tariff, 8 km. (5 miles)\n\n\n                  \n                      $31\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nPersonal Care\n\nUpdate prices\n\n\n\n\n\nCold medicine for 6 days (tylenol, frenadol, coldrex, or equivalent brands)\n\n\n                  \n                      $7\n                  \n                \n\n\n\n1 box of antibiotics (12 doses)\n\n\n                  \n                      $24\n                  \n                \n\n\n\nShort visit to private doctor (15 minutes)\n\n\n                  \n                      $163\n                  \n                \n\n\n\n1 box of 32 tampons (tampax, ob, ...)\n\n\n                  \n                      $8\n                  \n                \n\n\n\nDeodorant, roll-on (50ml ~ 1.5 oz.)\n\n\n                  \n                      $4.61\n                  \n                \n\n\n\nHair shampoo 2-in-1 (400 ml ~ 12 oz.)\n\n\n                  \n                      $8\n                  \n                \n\n\n\n4 rolls of toilet paper\n\n\n                  \n                      $4.81\n                  \n                \n\n\n\nTube of toothpaste\n\n\n                  \n                      $2.11\n                  \n                \n\n\n\nStandard men's haircut in expat area of the city\n\n\n                  \n                      $30\n                  \n                \n\nEntertainment\n\nUpdate prices\n\n\n\n\n\nBasic dinner out for two in neighborhood pub\n\n\n                  \n                      $63\n                  \n                \n\n\n\n2 tickets to the movies\n\n\n                  \n                      $32\n                  \n                \n\n\n\n2 tickets to the theater (best available seats)\n\n\n                  \n                      $397\n                  \n                \n\n\n\nDinner for two at an italian restaurant in the expat area including appetisers, main course, wine and dessert\n\n\n                  \n                      $114\n                  \n                \n\n\n\n1 cocktail drink in downtown club\n\n\n                  \n                      $16\n                  \n                \n\n\n\nCappuccino in expat area of the city\n\n\n                  \n                      $5.12\n                  \n                \n\n\n\n1 beer in neighbourhood pub (500ml or 1pt.) \n\n\n                  \n                      $7\n                  \n                \n\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n", '\n', '\n                  \n                      $32\n                  \n                ', '\n', '\n\n\n2 tickets to the theater (best available seats)\n\n\n                  \n                      $397\n                  \n                \n\n\n\nDinner for two at an italian restaurant in the expat area including appetisers, main course, wine and dessert\n\n\n                  \n                      $114\n                  \n                \n\n\n\n1 cocktail drink in downtown club\n\n\n                  \n                      $16\n                  \n                \n\n\n\nCappuccino in expat area of the city\n\n\n                  \n                      $5.12\n                  \n                \n\n\n\n1 beer in neighbourhood pub (500ml or 1pt.) \n\n\n                  \n                      $7\n                  \n                \n\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n']
# 1 beer in neighbourhood pub (500ml or 1pt.)
# ['\n', '\n                  \n                      $19\n                  \n                ', '\n', "\n\n\nCombo meal in fast food restaurant (big mac meal or similar)\n\n\n                  \n                      $10\n                  \n                \n\n\n\n500 gr (1 lb.) of boneless chicken breast\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 liter (1 qt.) of whole fat milk\n\n\n                  \n                      $1.28\n                  \n                \n\n\n\n12 eggs, large\n\n\n                  \n                      $4.52\n                  \n                \n\n\n\n1 kg (2 lb.) of tomatoes\n\n\n                  \n                      $4.60\n                  \n                \n\n\n\n500 gr (16 oz.) of local cheese\n\n\n                  \n                      $8\n                  \n                \n\n\n\n1 kg (2 lb.) of apples\n\n\n                  \n                      $3.52\n                  \n                \n\n\n\n1 kg (2 lb.) of potatoes\n\n\n                  \n                      $1.91\n                  \n                \n\n\n\n0.5 l (16 oz) domestic beer in the supermarket\n\n\n                  \n                      $4.23\n                  \n                \n\n\n\n1 bottle of red table wine, good quality\n\n\n                  \n                      $19\n                  \n                \n\n\n\n2 liters of coca-cola\n\n\n                  \n                      $2.53\n                  \n                \n\n\n\nBread for 2 people for 1 day\n\n\n                  \n                      $3.29\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nHousing\n\nUpdate prices\n\n\n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in expensive area\n\n\n                  \n                      $5,461\n                  \n                \n\n\n\nMonthly rent for 85 m2 (900 sqft) furnished accommodation in normal area\n\n\n                  \n                      $3,543\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 2 people in 85m2 flat\n\n\n                  \n                      $164\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in expensive area\n\n\n                  \n                      $3,516\n                  \n                \n\n\n\nMonthly rent for a 45 m2 (480 sqft) furnished studio in normal area\n\n\n                  \n                      $2,334\n                  \n                \n\n\n\nUtilities 1 month (heating, electricity, gas ...) for 1 person in 45 m2 (480 sqft) studio\n\n\n                  \n                      $126\n                  \n                \n\n\n\nInternet 8 mbps (1 month)\n\n\n                  \n                      $61\n                  \n                \n\n\n\n40” flat screen tv\n\n\n                  \n                      $320\n                  \n                \n\n\n\nMicrowave 800/900 watt (bosch, panasonic, lg, sharp, or equivalent brands)\n\n\n                  \n                      $182\n                  \n                \n\n\n\nLaundry detergent (3 l. ~ 100 oz.)\n\n\n                  \n                      $12\n                  \n                \n\n\n\nHourly rate for cleaning help\n\n\n                  \n                      $30\n                  \n                \n\n\n\n\n\n\n\nClothes\n\nUpdate prices\n\n\n\n\n\n1 pair of jeans (levis 501 or similar)\n\n\n                  \n                      $59\n                  \n                \n\n\n\n1 summer dress in a high street store (zara, h&m or similar retailers)\n\n\n                  \n                      $42\n                  \n                \n\n\n\n1 pair of sport shoes (nike, adidas, or equivalent brands)\n\n\n                  \n                      $92\n                  \n                \n\n\n\n1 pair of men’s leather business shoes\n\n\n                  \n                      $123\n                  \n                \n\nTransportation\n\nUpdate prices\n\n\n\n\n\nVolkswagen golf 1.4 tsi 150 cv (or equivalent), with no extras, new\n\n\n                  \n                      $22,801\n                  \n                \n\n\n\n1 liter (1/4 gallon) of gas\n\n\n                  \n                      $1.02\n                  \n                \n\n\n\nMonthly ticket public transport\n\n\n                  \n                      $128\n                  \n                \n\n\n\nTaxi trip on a business day, basic tariff, 8 km. (5 miles)\n\n\n                  \n                      $31\n                  \n                \n\n\n\nExpatistan is a collaborative effort. The data gets better with every new price that you enter.\n\n        We need your help!\n        \n          Tell us about prices in New York.\n      \n\n\n\n\n\n\nPersonal Care\n\nUpdate prices\n\n\n\n\n\nCold medicine for 6 days (tylenol, frenadol, coldrex, or equivalent brands)\n\n\n                  \n                      $7\n                  \n                \n\n\n\n1 box of antibiotics (12 doses)\n\n\n                  \n                      $24\n                  \n                \n\n\n\nShort visit to private doctor (15 minutes)\n\n\n                  \n                      $163\n                  \n                \n\n\n\n1 box of 32 tampons (tampax, ob, ...)\n\n\n                  \n                      $8\n                  \n                \n\n\n\nDeodorant, roll-on (50ml ~ 1.5 oz.)\n\n\n                  \n                      $4.61\n                  \n                \n\n\n\nHair shampoo 2-in-1 (400 ml ~ 12 oz.)\n\n\n                  \n                      $8\n                  \n                \n\n\n\n4 rolls of toilet paper\n\n\n                  \n                      $4.81\n                  \n                \n\n\n\nTube of toothpaste\n\n\n                  \n                      $2.11\n                  \n                \n\n\n\nStandard men's haircut in expat area of the city\n\n\n                  \n                      $30\n                  \n                \n\nEntertainment\n\nUpdate prices\n\n\n\n\n\nBasic dinner out for two in neighborhood pub\n\n\n                  \n                      $63\n                  \n                \n\n\n\n2 tickets to the movies\n\n\n                  \n                      $32\n                  \n                \n\n\n\n2 tickets to the theater (best available seats)\n\n\n                  \n                      $397\n                  \n                \n\n\n\nDinner for two at an italian restaurant in the expat area including appetisers, main course, wine and dessert\n\n\n                  \n                      $114\n                  \n                \n\n\n\n1 cocktail drink in downtown club\n\n\n                  \n                      $16\n                  \n                \n\n\n\nCappuccino in expat area of the city\n\n\n                  \n                      $5.12\n                  \n                \n\n\n\n1 beer in neighbourhood pub (500ml or 1pt.) \n\n\n                  \n                      $7\n                  \n                \n\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n", '\n', '\n                  \n                      $32\n                  \n                ', '\n', '\n\n\n2 tickets to the theater (best available seats)\n\n\n                  \n                      $397\n                  \n                \n\n\n\nDinner for two at an italian restaurant in the expat area including appetisers, main course, wine and dessert\n\n\n                  \n                      $114\n                  \n                \n\n\n\n1 cocktail drink in downtown club\n\n\n                  \n                      $16\n                  \n                \n\n\n\nCappuccino in expat area of the city\n\n\n                  \n                      $5.12\n                  \n                \n\n\n\n1 beer in neighbourhood pub (500ml or 1pt.) \n\n\n                  \n                      $7\n                  \n                \n\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n', '\n', '\n                  \n                      $7\n                  \n                ', '\n', '\n\n\nIpad wi-fi 128gb\n\n\n                  \n                      $418\n                  \n                \n\n\n\n1 min. of prepaid mobile tariff (no discounts or plans)\n\n\n                  \n                      $0.51\n                  \n                \n\n\n\n1 month of gym membership in business district\n\n\n                  \n                      $100\n                  \n                \n\n\n\n1 package of marlboro cigarettes\n\n\n                  \n                      $14\n                  \n                \n']

# USA Sibling
# '\n                  \n                      $19\n                  \n                '