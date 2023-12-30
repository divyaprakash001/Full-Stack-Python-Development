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
    
    # fetch one data using userid
    def fetch_by_id(self,id):
        query = f"select * from user where userId = {id}"
        cur = self.conn.cursor()
        cur.execute(query)
        
        for row in cur:
            print(row)
            print('User Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
    
    # fetch all data
    def fetch_all(self):
        query = 'select * from user'
        cur=self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            print('User Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
    
helper = DBHelper()
# helper.insert_data(236,'Mohan','9923364722')
# helper.fetch_all()
helper.fetch_by_id(235)