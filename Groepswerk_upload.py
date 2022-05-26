from SQL_functions import *
from Scraping_functions import *
from time import sleep

# Define the starting point and end point of the loop
start_id = 248
end_id = 249


# Loop through the cities
for city_id in range(start_id, end_id):
      # Load the city names and country from the database table 'city' and 'country' ( via SQL functions)
      sql = f"select name_climate, name_expat, name_numbeo, co_name as country from city left join country c on c.co_id = city.ci_co_id where ci_id = {city_id}"
      city_names = get_data(sql)
      print(city_id, ':' ,city_names)

      # Scrape climate data (via Scraping functions)
      temp_data, rain_data, sun_data = climate(city_names[0], city_names[3])
      print('temp:', temp_data); print('rain:', rain_data); print('sun:', sun_data)
      # Load climate data into database (via SQL functions)
      for y in range(0, 24, 2):
            # Temperature data
            for x in range(2):
                  sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = {x + 1}, da_mo_id = {(y + 2) / 2}, da_value = {temp_data[y + x]}"
                  dbase_insert(sql)
            # Rain data
            for x in range(2):
                  sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = {x + 3}, da_mo_id = {(y + 2) / 2}, da_value = {rain_data[y + x]}"
                  dbase_insert(sql)
      # Sun data
      for index, value in enumerate(sun_data):
            sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = 5, da_mo_id = {index + 1}, da_value = {value}"
            dbase_insert(sql)

      # Scrape cost of living data (via Scraping functions)
      expat_data = expat(city_names[1], city_names[3])
      print('cost of living:', expat_data)
      # Load cost of living data into database (via SQL functions)
      for index, value in enumerate(expat_data):
            sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = {index + 6 }, da_mo_id = 13, da_value = {value}"
            dbase_insert(sql)

      # Scrape crime data (via Scraping functions)
      numbeo_crime_data = numbeo_crime(city_names[2])
      print('crime:', numbeo_crime_data)
      # Load crime data into database (via SQL functions)
      for index, value in enumerate(numbeo_crime_data):
            sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = {index + 23 }, da_mo_id = 13, da_value = {value}"
            dbase_insert(sql)

      # Scrape pollution data (via Scraping functions)
      numbeo_pollution_data = numbeo_pollution(city_names[2])
      print('pollution:', numbeo_pollution_data)
      # Load pollution data into database (via SQL functions)
      for index, value in enumerate(numbeo_pollution_data):
            sql = f"INSERT INTO data SET da_ci_id = {city_id}, da_spec_id = {index + 31}, da_mo_id = 13, da_value = {value}"
            dbase_insert(sql)

      sleep(5)



# output
#
# ('perth', 'perth', 'Perth', 'Australia')
#
# temp: ['18', '32', '18', '32', '16', '30', '14', '26', '11', '22', '9', '20', '8', '18', '8', '19', '9', '21', '11', '24', '13', '27', '16', '30']
# rain: ['15', '1', '15', '1', '20', '2', '30', '4', '80', '9', '125', '12', '140', '14', '120', '13', '80', '11', '35', '5', '30', '4', '10', '2']
# sun: ['355', '320', '300', '250', '205', '175', '190', '225', '230', '300', '320', '355']
# sun is index + 5
# cost of living: ['15', '25', '7', '1444', '1166', '1271', '867', '262', '153', '176.0', '61.5', '116', '63', '108', '3.96', '11', '1.94']
# cost of living is index 6 to 22
# crime: ['43.99', '42.13', '33.66', '30.39', '40.14', '55.04', '76.35', '43.04']
# crime is index 23 to 30
# pollution: ['23.14', '17.06', '13.94', '26.29', '31.79', '82.04', '83.10']
# pollution is index 31 to 37

