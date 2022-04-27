import mysql.connector as mysql
from SQL_functions import *

city = 11
spec = 3
data =  [15,17,20,19,18,17,15,14,12,11,10,11 ]


for index, value in enumerate(data):
      sql = f"INSERT INTO data SET da_ci_id = {city}, da_spec_id = {spec}, da_mo_id = {index +1}, da_value = {value}"
      if dbase_insert(sql): pass
      else: print(f"Er liep iets fout bij het updaten van de database in maand {index +1}")

