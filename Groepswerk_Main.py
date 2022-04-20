import mysql.connector as mysql
from SQL_functions import *

list = ['ci_name', 'ci_name2', 'ci_population', 'ci_co_id',
        'ci_mintemp_jan', 'ci_mintemp_feb', 'ci_mintemp_mar', 'ci_mintemp_apr', 'ci_mintemp_may', 'ci_mintemp_jun',
        'ci_maxtemp_jan', 'ci_maxtemp_feb', 'ci_maxtemp_mar', 'ci_maxtemp_apr', 'ci_maxtemp_may', 'ci_maxtemp_jun'    ]
data = ['Mumbai', 'Bombay', 20961465, 1, 15,17,20,23,26,25,30,31,32,32,33,25 ]


for x in range(4, 16):
      sql = f"UPDATE city SET {list[x]} = '{data[x]}' WHERE ci_id=2"
      if dbase_update(sql): pass
      else: print(f"Er liep iets fout bij het updaten van de database in kolom {key}")



#
#
# dict = get_dict()
#
# for key,value in dict.items():
#       sql = f"UPDATE city SET {key} = '{value}' WHERE ci_id=2"
#       if dbase_update(sql): pass
#       else: print(f"Er liep iets fout bij het updaten van de database in kolom {key}")
#
