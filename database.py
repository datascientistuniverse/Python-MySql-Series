# Import library
import mysql.connector

# Make connection
mydb = mysql.connector.connect(host= "localhost", user= "root", password= "root@123")
print(mydb)
