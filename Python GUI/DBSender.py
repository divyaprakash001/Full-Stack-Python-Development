import mysql.connector as connector

class DBHelper:
    # using class constructor to initialize and create connection object here
    def __init__(self):
        self.conn = connector.connect(host='localhost',port='3306',user='root',password='data73063',database='divya')
        query = 'create table if not exists employee(eid int NOT NULL AUTO_INCREMENT, ename varchar(25),post varchar(20), gender varchar(10), state varchar(25) ,address varchar(300), PRIMARY KEY (`eid`))'
        cur = self.conn.cursor()
        cur.execute(query)
        print('table created if not exist')
    
    # insert data
    def insert_data(self,ename,post,gender,state,address):
        query = f"insert into employee( ename, post, gender, state, address) values('{ename}','{post}','{gender}','{state}','{address}')"
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("user data inserted")
    
    # fetch one data using userid
    def fetch_by_id(self,id):
        query = f"select * from employee where eid = {id}"
        cur = self.conn.cursor()
        cur.execute(query)
        
        for row in cur:
            print(row)
            print('Employee Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
    
    # fetch all data
    def fetch_all(self):
        query = 'select * from employee'
        cur=self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            print('User Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
           
    # delete the data
    def delete_data(self,id):
        query = f"delete from employee where eid = {id}"
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print('deleted')

    # updata the data using userId
    def updata_data(self,id, newName, newPost, newGender, newState, newAddress):
        query = f"update employee set ename='{newName}', post='{newPost}','{newGender}','{newState}','{newAddress}' where eid = {id}"
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated")
