import mysql.connector as mysql

def get_dict():
    return {
        'ci_name': "Mumbai",
        'ci_name2': "Bombay",
        'ci_population': 20961472,
        'ci_co_id': 2,
        'ci_mintemp_jan': 17,
        'ci_mintemp_feb': 18,
        'ci_mintemp_mar': 21,
        'ci_mintemp_apr': 24,
        'ci_mintemp_may': 27,
        'ci_mintemp_jun': 26,
        'ci_maxtemp_jan': 31,
        'ci_maxtemp_feb': 32,
        'ci_maxtemp_mar': 33,
        'ci_maxtemp_apr': 33,
        'ci_maxtemp_may': 34,
        'ci_maxtemp_jun': 32
    }


def get_config():
    dbase = 'test_cities'
    return {
        'user': 'root',
        'password': 'xxxxxxxx',
        'host': '127.0.0.1',
        'database': dbase,
        'raise_on_warnings': True
        }  # dit is local host


def get_data(sql):

    config = get_config()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    data = []
    for row in cursor:
        data.append(row)

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
