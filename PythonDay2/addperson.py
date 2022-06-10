import pymysql
from dbpackage import ConnectMySQL as con


def add_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
        INSERT INTO person(fullname,weight,height) 
        VALUES('สามิตร โกยม','60','165')
    """
    try:
        cursor.execute(sql)
        connection.commit()
        print("Add person succcess")
    except pymysql.err:
        print(pymysql.err)


add_person()        