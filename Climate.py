from bs4 import BeautifulSoup, Tag
import requests

country_only =  [ 'yerevan','baku','manama','bujumbura','phnom penh','djibouti','santo domingo','san salvador','tbilisi','guatemala city','port au prince','hong kong','tehran','baghdad','tel aviv','kingston',
    'astana','kuwait city','beirut','monrovia','macao','lilongwe','kuala lumpur','ulaanbaatar','kathmandu','auckland','managua','muscat','panama city','manila','san juan','doha','riyadh','freetown','singapore',
    'taibei','port of spain','tashkent','ho chi minh city','hanoi','lusaka'  ]



country = "new zealand"
country = country.replace(' ', '-')
city = "auckland"
city = city.replace(' ', '-')
insert = country + '/' + city

if city in country_only:
    insert = country


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}

response = requests.get('https://www.climatestotravel.com/climate/' + insert, headers=headers, timeout=8)

try:
    response.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))

soup = BeautifulSoup(response.text, 'html.parser')



print("temperature: ")
temp_table = soup.find('tr', "min-table").parent
for month in temp_table.find_all('th', scope="row"):
    print(month.get_text())
    for temp in month.parent.find_all('td', limit=2):
        print(temp.get_text())

print(); print()
print("precipitation: ")
precipit_table = soup.find('tr', "precipit-table").parent
for month in precipit_table.find_all('th', scope="row"):
    print(month.get_text())
    for precipit in month.parent.find_all('td'):
        print(precipit.get_text())

# best_months = soup.find('span', id="best_time").parent.next_sibling.next_sibling.next_sibling
best_month = ''
x = 0
for sibling in soup.find('span', id="best_time").parent.next_siblings:
    x += 1
    text = str(sibling)
    if len(text) > 5:                  # ignore spam such as '\n' , <br>,... and only keep the long text
        best_month += text
    if x == 10: break
best_month = best_month.replace('<strong>', '')
best_month = best_month.replace('</strong>', '')
best_month = best_month.replace('\n', ' ')
print(); print("Best Month: \n", best_month)
print()

all_data = []
sunshine_list = []

table = soup.find('table', class_="sole")
for child in table.children:
    if isinstance(child, Tag):
         all_data.append(child.get_text())
for x in range(4, 40, 3):
    sunshine_list.append(all_data[x])
print('sunshine : ')
print(sunshine_list)


# print(soup.prettify())
# sunshine line 964


#
# month =
# <th scope="row" title="January">January</th>
# <th scope="row" title="February">February</th>
# <th scope="row" title="March">March</th>

# print(temp_table.get_text())
# temperatures = temp_table.find_all('td')
# print(temperatures)
# caption = temp_table.caption
# print(caption.text)
#

# result = []
# for child in soup.find('tr', "min-table").parent.next_siblings:
#     if child != '\n':
#         result.append(child.string)
#
# print(result)


# .parent gives you the 'find' and everything below
# tables = soup.find('tr', "min-table").parent
# <table class="cities"><caption>Mumbai - Average temperatures (1991-2020) </caption><colgroup><col/><col class="celsius" span="3"/><col class="fahrenheit" span="3"/></colgroup><tr class="title-table-new"><th scope="col">Month</th><th scope="col" title="Average low temperatures (degrees Celsius)">Min (°C)</th><th scope="col" title="Average high temperatures (degrees Celsius)">Max (°C)</th><th scope="col" title="Average daily temperature (degrees Celsius)">Mean (°C)</th><th scope="col" title="Average low temperatures (degrees Fahrenheit)">Min (°F)</th><th scope="col" title="Average high temperatures (degrees Fahrenheit)">Max (°F)</th><th scope="col" title="Average daily temperature (degrees Fahrenheit)">Mean (°F)</th></tr><tr class="min-table"><th scope="row" title="January">January</th><td>17</td><td>31</td><td>24</td><td>62</td><td>88</td><td>75.3</td></tr><tr class="min-table"><th scope="row" title="February">February</th><td>18</td><td>32</td><td>25</td><td>65</td><td>89</td><td>77</td></tr><tr class="min-table"><th scope="row" title="March">March</th><td>21</td><td>33</td><td>27.2</td><td>70</td><td>92</td><td>80.9</td></tr><tr class="min-table"><th scope="row" title="April">April</th><td>24</td><td>33</td><td>28.8</td><td>75</td><td>92</td><td>83.9</td></tr><tr class="min-table"><th scope="row" title="May">May</th><td>27</td><td>34</td><td>30.2</td><td>80</td><td>93</td><td>86.4</td></tr><tr class="min-table"><th scope="row" title="June">June</th><td>26</td><td>32</td><td>29.4</td><td>79</td><td>90</td><td>85</td></tr><tr class="min-table"><th scope="row" title="July">July</th><td>25</td><td>30</td><td>27.9</td><td>78</td><td>87</td><td>82.2</td></tr><tr class="min-table"><th scope="row" title="August">August</th><td>25</td><td>30</td><td>27.8</td><td>77</td><td>87</td><td>82</td></tr><tr class="min-table"><th scope="row" title="September">September</th><td>25</td><td>31</td><td>28</td><td>77</td><td>88</td><td>82.3</td></tr><tr class="min-table"><th scope="row" title="October">October</th><td>24</td><td>34</td><td>28.8</td><td>75</td><td>93</td><td>83.8</td></tr><tr class="min-table"><th scope="row" title="November">November</th><td>21</td><td>34</td><td>27.8</td><td>71</td><td>93</td><td>82</td></tr><tr class="min-table"><th scope="row" title="December">December</th><td>18</td><td>33</td><td>25.5</td><td>65</td><td>91</td><td>77.8</td></tr><tr class="min-table"><th scope="row" title="Year">Year</th><td>22.7</td><td>32.4</td><td>27.5</td><td>72.9</td><td>90.3</td><td>81.5</td></tr></table>
# extract
# Fahrenheit)">Mean (°F)</th></tr><tr class="min-table"><th scope="row" title="January">January</th><td>17</td><td>31</td><td>24</td><td>62</td><td>88</td><td>75.3</td></tr><tr class="min-table"><th scope="row" title="February">February</th><td>18</td><td>32</

# sunshine_table = soup.find('table', class_="sole")
# print(sunshine_table)
# sunshine table : only up to january:
# <div class="div-tabella"><table class="sole"><caption>Mumbai - Sunshine hours</caption><tr class="title-table-new"><th scope="col">Month</th><th scope="col" title="Average daily sunshine hours">Average</th><th scope="col">Total</th></tr><th scope="row" title="January">January</th><td>9</td><td>280</td></table></div>

# extract from 'soup' : after January there is a lot of bullshit, which makes it impossible to capture the full sole table
# therefore we capture sunshine from an other website
# <div class="div-tabella"><table class="sole"><caption>Mumbai - Sunshine hours</caption><tr class="title-table-new"><th scope="col">Month</th><th scope="col" title="Average daily sunshine hours">Average</th><th scope="col">Total</th></tr>
# <th scope="row" title="January">January</th><td>9</td><td>280</td></table></div></div></div></div></form></body></html>
# <th scope="row" title="February">February</th><td>9.5</td><td>275</td>
# <th scope="row" title="March">March</th><td>9</td><td>280</td>
# <th scope="row" title="April">April</th><td>9.5</td><td>280</td>
# <th scope="row" title="May">May</th><td>9</td><td>275</td>
# <th scope="row" title="June">June</th><td>4.5</td><td>140</td>
# <th scope="row" title="July">July</th><td>2.5</td><td>80</td>
# <th scope="row" title="August">August</th><td>2.5</td><td>80</td>
# <th scope="row" title="September">September</th><td>5</td><td>145</td>
# <th scope="row" title="October">October</th><td>7.5</td><td>240</td>
# <th scope="row" title="November">November</th><td>9</td><td>265</td>
# <th scope="row" title="December">December</th><td>9</td><td>275</td>
# <th scope="row" title="Year">Year</th><td>7.2</td><td>2615</td>
# <br/>

#
# datalist = []
# table = soup.find('table', class_="sole")
# for child in table.children:
#     datalist.append(child)
# print(datalist)
# output:
# [
# <caption>Mumbai - Sunshine hours</caption>,
# <tr class="title-table-new"># <th scope="col">Month</th># <th scope="col" title="Average daily sunshine hours">Average</th># <th scope="col">Total</th># </tr>,
# <th scope="row" title="January">January</th>,
# <td>9</td>,
# <td>280</td>,
# <th scope="row" title="February">February</th>,
# <td>9.5</td>,
# <td>275</td>,
# <th scope="row" title="March">March</th>, <td>9</td>, <td>280</td>, <th scope="row" title="April">April</th>, <td>9.5</td>, <td>280</td>, <th scope="row" title="May">May</th>, <td>9</td>, <td>275</td>, <th scope="row" title="June">June</th>, <td>4.5</td>, <td>140</td>, <th scope="row" title="July">July</th>, <td>2.5</td>, <td>80</td>, <th scope="row" title="August">August</th>, <td>2.5</td>, <td>80</td>, <th scope="row" title="September">September</th>, <td>5</td>, <td>145</td>, <th scope="row" title="October">October</th>, <td>7.5</td>, <td>240</td>, <th scope="row" title="November">November</th>, <td>9</td>, <td>265</td>, <th scope="row" title="December">December</th>, <td>9</td>, <td>275</td>, <th scope="row" title="Year">Year</th>, <td>7.2</td>, <td>2615</td>]
#
# but : table.find('td') did not work ; output was 'None'

# datalist = []
# table = soup.find('table', class_="sole")
# for child in table.children:
#     if isinstance(child, Tag):
#          datalist.append(child.get_text())
# print(datalist)
# output:
# ['Mumbai - Sunshine hours', 'MonthAverageTotal', 'January', '9', '280', 'February', '9.5', '275', 'March', '9', '280', 'April', '9.5', '280', 'May', '9', '275', 'June', '4.5', '140', 'July', '2.5', '80', 'August', '2.5', '80', 'September', '5', '145', 'October', '7.5', '240', 'November', '9', '265', 'December', '9', '275', 'Year', '7.2', '2615']
#
