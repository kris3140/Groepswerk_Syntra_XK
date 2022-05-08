import pandas as pd

#  database://user:password@host/dbname
my_conn = 'mysql://py_xavier:pk6pMJXXj83n@185.115.218.166/py_xavier'

city_id = 54
sql = f"select name_climate as city, sp_short as spec, td_value as value, mo_short as month, sp_long as description from testdata " \
      f"left join city c on testdata.td_ci_id = c.ci_id  " \
      f"left join spec s on testdata.td_spec_id = s.sp_id " \
      f"left join months m on testdata.td_mo_id = m.mo_id " \
      f"where ci_id = {city_id}"

city1 = pd.read_sql(sql, my_conn)

print(city1[['city', 'spec', 'value', 'month', 'description']])
# print(city1.to_string())

