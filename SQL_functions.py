import mysql.connector as mysql


def Db_create_record(city):
    sql = f"INSERT INTO cities SET ci_datumtijd=NOW(), ci_name='{city}'"
    city_id = DBInsert(sql)
    return city_id


def Db_insert_data(city_id, data):
    sql = f"UPDATE cities SET ci_temp_jan='{data}' where ci_id={city_id}"
    if DBUpdate(sql):
        pass
    else:
        print("Er liep iets fout bij het updaten van de database")


def Db_get_data(city_name):
    sql = f"SELECT * FROM cities LEFT JOIN countries ON cities.ci_id = countries.co_ci_id WHERE ci_name={city_name}"
    data = GetData(sql)
    return data



def GetConfig():
    return {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'mastermind',
        'raise_on_warnings': True,
    }


def GetData(sql):

    config = GetConfig()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    data = []
    for row in cursor:
        data.append(row)

    cursor.close()
    cnx.close()

    return data


def DBInsert(sql):
    config = GetConfig()
    cnx = mysql.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql)

    cnx.commit()

    # print( f"Record with id {cursor.lastrowid} inserted.")

    cursor.close()
    cnx.close()

    return cursor.lastrowid


def DBUpdate(sql):
    config = GetConfig()
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
