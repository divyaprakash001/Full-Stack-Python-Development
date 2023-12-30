import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.conn = connector.connect(host='localhost',port='3306',user='root',password='data73063',database='divya')
        query = 'create table if not exists user(userId int primary key, userName varchar(25), phone varchar(13))'
        cur = self.conn.cursor()
        cur.execute(query)
        print('table created')
    
x = DBHelper()