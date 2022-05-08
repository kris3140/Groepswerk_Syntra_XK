from SQL_functions import *
from Scraping_functions import *
from time import sleep


start_id = 46
end_id = 47

for x in range(start_id, end_id):
      sql = f"select name_climate, name_expat, name_numbeo, co_name as country from city left join country c on c.co_id = city.ci_co_id where ci_id = {start_id}"
      city_names = get_data(sql)
      print(city_names)

      # climate_data = climate(city_names[0], city_names[3])
      # print(climate_data)
      # expat_data = expat(city_names[1], city_names[3])
      # print(expat_data)
      # numbeo_crime_data = numbeo_crime(city_names[2])
      # print(numbeo_crime_data)
      numbeo_pollution_data = numbeo_pollution(city_names[2])
      print(numbeo_pollution_data)

      sleep(1)




# output get_data()
# city_names = ('tirana', 'tirana', 'Tirana', 'Albania')

# output climate()
# climate_data = ['2', '12', '3', '14', '6', '17', '9', '20', '13', '25', '17', '29',  = min and max temp jan to jun  index 0 to 11
#                '19', '32', '18', '33', '15', '28', '11', '23', '7', '18', '3', '14',  = min and max temp jul to dec  index 12 to 23
#                '10.1', '22.2',   = min and max temp year index 24 to 25
#                '135', '10', '150', '10', '130', '11', '115', '10', '120', '9', '85', '5',  = prec mm and days jan to jun   index 26 to 37
#                '30', '4', '30', '3', '60', '5', '105', '7', '210', '12', '175', '12', = prec mm and days jul to dec   index 38 to 49
#                '1345', '98', = prec mm and days year  index 50 and 51
#                '125', '125', '165', '190', '265', '300', '355', '325', '265', '220', '125', '90' = sunshine hours per month  index 52 to 63
#               ]

# output expat()
# expat_data = ['8', '14', '2.76', '356', '92', '105', '5.08', '1.73', '14', '53', '89', '2.71', '12', '1.37']
# from index 0 to 13 = from sp_id 6 to 19

# output numbeo_crime()
# numbeo_crime_data = ['46.82', '40.57', '42.04', '41.25', '36.31', '37.89', '50.76', '71.88', '54.27']
# from index 0 to 8 = from sp_id 20 to 28

# numbeo_pollution()
# numbeo_pollution_data = ['87.94', '81.67', '74.75', '69.66', '59.00', '72.50', '30.00', '31.80']
# # from index 0 to 7 = from sp_id 29 to 36





# city = 11
# spec = 3
# data =  [15,17,20,19,18,17,15,14,12,11,10,11 ]
#
#
# for index, value in enumerate(data):
#       sql = f"INSERT INTO data SET da_ci_id = {city}, da_spec_id = {spec}, da_mo_id = {index +1}, da_value = {value}"
#       if dbase_insert(sql): pass
#       else: print(f"Er liep iets fout bij het updaten van de database in maand {index +1}")

