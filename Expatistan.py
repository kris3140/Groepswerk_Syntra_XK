from bs4 import BeautifulSoup
import requests

# changes to be made for USD prices if country is USA
country = 'france'
city = "lyon"

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
chicken = soup.find('a', text='500 gr (1 lb.) of boneless chicken breast')

data_elements = [lunch, chicken]

print(f'{country} / {city}: ')
for element in data_elements:
    print(element.get_text())
    x = 0
    for line in element.parent.next_siblings:
        x += 1
        try:
            usd = line.find('i')
            print(usd.get_text())
        except:
            continue
        if x == 4: break










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


