import psycopg2

connection = psycopg2.connect(user="morzloof",
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="morzloof")
connection.autocommit = True

def querySelect(sql):
    cur = connection.cursor()
    try:
        cur.execute(sql)
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))
    res = None

    try:
        res = cur.fetchall()
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))
    cur.close()
    
    return res

def queryInsert(sql):
    cur = connection.cursor()
    try:
        cur.execute(sql)
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))

    res = None
    cur.close()
    
    return res