# https://dev.mysql.com/downloads/file/?id=484755
import mysql.connector

class CreateTable:

  def connectdb(self):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="8xPm2vad",
      port=3307,
      database="world"
    )
    print(mydb)
    return mydb

  def createtable(self):

    queries=['CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))','describe customers']
    mydb=CreateTable.connectdb(self)
    cursor=mydb.cursor()
    cursor.execute("show tables")
    flag=0
    for table in cursor:
        if "customers" in table:
            print("table customers found")
            flag=1
            break
    if flag is 0:
        for q in queries:
            cursor.execute(q)
            for x in cursor:
                print(x)
    return mydb

  def insert_a_value(self):

      mydb=CreateTable.createtable(self)
      cursor = mydb.cursor()
      sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
      val = ("John", "Highway 21")
      cursor.execute(sql, val)
      mydb.commit()
      print(cursor.rowcount, "record inserted.")
      return mydb

  def insert_multiple_value(self):

      mydb=CreateTable.createtable(self)
      cursor = mydb.cursor()
      sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
      val = [
          ('Peter', 'Lowstreet 4'),
          ('Amy', 'Apple st 652'),
          ('Hannah', 'Mountain 21'),
          ('Michael', 'Valley 345'),
          ('Sandy', 'Ocean blvd 2'),
          ('Betty', 'Green Grass 1'),
          ('Richard', 'Sky st 331'),
          ('Susan', 'One way 98'),
          ('Vicky', 'Yellow Garden 2'),
          ('Ben', 'Park Lane 38'),
          ('William', 'Central st 954'),
          ('Chuck', 'Main Road 989'),
          ('Viola', 'Sideway 1633')
      ]
      cursor.executemany(sql, val)
      mydb.commit()
      print(cursor.rowcount, "record inserted.")
      return mydb

  def read_table(self):

      mydb=CreateTable.insert_a_value(self)
      cursor=mydb.cursor()
      cursor.execute("select * from customers")
      for x in cursor:
          print(x)

if __name__ ==  "__main__":
  db=CreateTable()
  db.connectdb()
  db.createtable()
  db.insert_a_value()
  db.insert_multiple_value()
  db.read_table()
