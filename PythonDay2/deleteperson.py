import pymysql
from dbpackage import ConnectMySQL as con


def delete_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
        DELETE FROM person WHERE id='1'
    """
    try:
        cursor.execute(sql)
        connection.commit()
        print("Delete person succcess")
    except pymysql.err:
        print(pymysql.err)


delete_person()    