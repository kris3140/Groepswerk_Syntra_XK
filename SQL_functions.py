import mysql.connector as mysql
import pandas as pd


def get_config():
     return {
        'user': 'py_xavier',
        'password': 'pk6pMJXXj83n',
        'host': '185.115.218.166',
        'database': 'py_xavier',
        'raise_on_warnings': True
        }

def get_data(sql):

    config = get_config()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor()   #(dictionary=True)
    cursor.execute(sql)

    for row in cursor:
        data = row

    cursor.close()
    cnx.close()

    return data


def dbase_insert(sql):
    config = get_config()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    cnx.commit()

    # print( f"Record with id {cursor.lastrowid} inserted.")

    cursor.close()
    cnx.close()

    return cursor.lastrowid


def dbase_update(sql):
    config = get_config()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)

    try:
        cursor.execute(sql)
        cnx.commit()
        aantal_records_geupdated = cursor.rowcount
        cursor.close()
        cnx.close()
        return True
    except:
        return False


def get_pandas(city):
    #  database://user:password@host/dbname
    my_conn = 'mysql://py_xavier:pk6pMJXXj83n@185.115.218.166/py_xavier'


    sql = f"select name_climate as city, sp_short as spec, da_value as value, mo_short as month, sp_long as description, sp_measure as measure from data " \
          f"left join city c on data.da_ci_id = c.ci_id  " \
          f"left join spec s on data.da_spec_id = s.sp_id " \
          f"left join months m on data.da_mo_id = m.mo_id " \
          f"where name_climate = '{city}'"

    return pd.read_sql(sql, my_conn)



#
#
# def Db_create_record(city):
#     sql = f"INSERT INTO cities SET ci_datumtijd=NOW(), ci_name='{city}'"
#     city_id = DBInsert(sql)
#     return city_id
#
#
# def Db_insert_data(city_id, data):
#     sql = f"UPDATE cities SET ci_temp_jan='{data}' where ci_id={city_id}"
#     if DBUpdate(sql):
#         pass
#     else:
#         print("Er liep iets fout bij het updaten van de database")
#
#
# def Db_get_data(city_name):
#     sql = f"SELECT * FROM cities LEFT JOIN countries ON cities.ci_id = countries.co_ci_id WHERE ci_name={city_name}"
#     data = GetData(sql)
#     return data
#



