from SQL_functions import *
from Scraping_functions import *
from time import sleep

# Define the starting point and end point of the loop
start_id = 55
end_id = 56

# Loop through the cities
for city_id in range(start_id, end_id):
      # Load the city names and country from the database table 'city' and 'country' ( via SQL functions)
      sql = f"select name_climate, name_expat, name_numbeo, co_name as country from city left join country c on c.co_id = city.ci_co_id where ci_id = {city_id}"
      city_names = get_data(sql)
      print(city_names)

      # Scrape climate data (via Scraping functions)
      temp_data, rain_data, sun_data = climate(city_names[0], city_names[3])
      print('temp:', temp_data); print('rain:', rain_data); print('sun:', sun_data)
      # Load climate data into database (via SQL functions)
      for y in range(0, 24, 2):
            # Temperature data
            for x in range(2):
                  sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = {x + 1}, td_mo_id = {(y + 2) / 2}, td_value = {temp_data[y + x]}"
                  dbase_insert(sql)
            # Rain data
            for x in range(2):
                  sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = {x + 3}, td_mo_id = {(y + 2) / 2}, td_value = {rain_data[y + x]}"
                  dbase_insert(sql)
      # Sun data
      for index, value in enumerate(sun_data):
            sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = 5, td_mo_id = {index + 1}, td_value = {value}"
            dbase_insert(sql)

      # Scrape cost of living data (via Scraping functions)
      expat_data = expat(city_names[1], city_names[3])
      print('cost of living:', expat_data)
      # Load cost of living data into database (via SQL functions)
      for index, value in enumerate(expat_data):
            sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = {index + 6 }, td_mo_id = 13, td_value = {value}"
            dbase_insert(sql)

      # Scrape crime data (via Scraping functions)
      numbeo_crime_data = numbeo_crime(city_names[2])
      print('crime:', numbeo_crime_data)
      # Load crime data into database (via SQL functions)
      for index, value in enumerate(numbeo_crime_data):
            sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = {index + 20 }, td_mo_id = 13, td_value = {value}"
            dbase_insert(sql)

      # Scrape pollution data (via Scraping functions)
      numbeo_pollution_data = numbeo_pollution(city_names[2])
      print('pollution:', numbeo_pollution_data)
      # Load pollution data into database (via SQL functions)
      for index, value in enumerate(numbeo_pollution_data):
            sql = f"INSERT INTO testdata SET td_ci_id = {city_id}, td_spec_id = {index + 29 }, td_mo_id = 13, td_value = {value}"
            dbase_insert(sql)

      sleep(1)




# output get_data()
# city_names = ('tirana', 'tirana', 'Tirana', 'Albania')

# output climate()
# temp_data = ['2', '12', '3', '14', '6', '17', '9', '20', '13', '25', '17', '29', '19', '32', '18', '33', '15', '28', '11', '23', '7', '18', '3', '14']
# index even and uneven = sp_id 1 and 2
# rain_data = ['135', '10', '150', '10', '130', '11', '115', '10', '120', '9', '85', '5', '30', '4', '30', '3', '60', '5', '105', '7', '210', '12', '175', '12']
# index even and uneven = sp_id  3 and 4
# sun_data = ['125', '125', '165', '190', '265', '300', '355', '325', '265', '220', '125', '90']
# sp_id = 5

# output expat()
# expat_data = ['8', '14', '2.76', '356', '92', '105', '5.08', '1.73', '14', '53', '89', '2.71', '12', '1.37']
# from index 0 to 13 = from sp_id 6 to 19

# output numbeo_crime()
# numbeo_crime_data = ['46.82', '40.57', '42.04', '41.25', '36.31', '37.89', '50.76', '71.88', '54.27']
# from index 0 to 8 = from sp_id 20 to 28

# output numbeo_pollution()
# numbeo_pollution_data = ['87.94', '81.67', '74.75', '69.66', '59.00', '72.50', '30.00', '31.80']
# # from index 0 to 7 = from sp_id 29 to 36


# for index, value in enumerate(data):
#       sql = f"INSERT INTO data SET da_ci_id = {city}, da_spec_id = {spec}, da_mo_id = {index +1}, da_value = {value}"
#       if dbase_insert(sql): pass
#       else: print(f"Er liep iets fout bij het updaten van de database in maand {index +1}")

