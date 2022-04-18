import mysql.connector as mysql
from SQL_functions import *


dict = get_dict()

for key,value in dict.items():
      sql = f"UPDATE city SET {key} = '{value}' WHERE ci_id=2"
      if dbase_update(sql): pass
      else: print(f"Er liep iets fout bij het updaten van de database in kolom {key}")