import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()
mycursor.execute("SHOW COLUMNS FROM housedb")
# mycursor.execute(
#    "CREATE TABLE HouseDB (id int PRIMARY KEY AUTO_INCREMENT, listing_name varchar(255) NOT NULL, " +
#    "price varchar(255) NOT NULL, location varchar(255) NOT NULL, description varchar(1000) NOT NULL, " +
#    "contact varchar(255) NOT NULL, image varchar(500))" +
#    ")")
for x in mycursor:
    print(x)
