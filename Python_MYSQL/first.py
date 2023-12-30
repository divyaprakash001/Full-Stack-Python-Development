import mysql.connector as connector

conn = connector.connect(host='localhost',port='3306',user='root',password='data73063',database='divya')

print(conn)