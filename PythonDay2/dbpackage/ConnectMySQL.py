import pymysql

def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='pythondemodb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# print(connectdb())