import pymysql
from dbpackage import ConnectMySQL as con


def edit_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
        UPDATE person SET 
        weight='55',
        height='150' 
        WHERE id='1'
    """
    try:
        cursor.execute(sql)
        connection.commit()
        print("Edit person succcess")
    except pymysql.err:
        print(pymysql.err)


edit_person()        