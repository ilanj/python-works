# https://dev.mysql.com/downloads/file/?id=484755
import mysql.connector


class ConnectDB:

    def connectdb(self):
        mydb = mysql.connector.connect(
            host="localhost", user="root", passwd="8", port=3307, database="world"
        )
        print(mydb)
        return mydb

    def readvalues(self):
        mydb = ConnectDB.connectdb(self)
        cursor = mydb.cursor()
        cursor.execute("select * from countrylanguage")
        for x in cursor:
            print(x)


if __name__ == "__main__":
    db = ConnectDB()
    db.connectdb()
    db.readvalues()
