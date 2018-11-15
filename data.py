import mysql.connector

mydb = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='Pinina89',
		# database='gen'
		# )

#print(mydb)



#^ 2 interact w data base 

mycursor = mydb.cursor()
# ^ obj allows interct w db tables 

mycursor.execute("CREATE DATABASE gen")

# print(mycursor.execute("SHOW DATABASES"))


print(mycursor.execute("SELECT DATABASE()"))
# for x in mycursor:
# 	print(x)