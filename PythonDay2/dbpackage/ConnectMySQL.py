import pymysql

def connectdb():
    return pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='pythondemodb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )


# print(connectdb())