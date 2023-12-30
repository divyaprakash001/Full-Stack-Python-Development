import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.conn = connector.connect(host='localhost',port='3306',user='root',password='data73063',database='divya')
        query = 'create table if not exists user(userId int primary key, userName varchar(25), phone varchar(13))'
        cur = self.conn.cursor()
        cur.execute(query)
        print('table created')
    
    # insert data
    def insert_data(self,userId, userName, phone):
        query = f"insert into user(userId, userName, phone) values({userId},'{userName}','{phone}')"
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("user data inserted")
    
helper = DBHelper()
helper.insert_data(235,'Mohit','6237364722')