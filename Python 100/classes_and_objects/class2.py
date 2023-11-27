class Users:
    def __init__(self,name,age,fname,mname,gender,address):
        print('you are in Users constructor')
        self.name=name
        self.age=age
        self.fname=fname
        self.mname=mname
        self.gender=gender
        self.address=address
    def UserInfo(self):
        try:
            print(f'Hey {self.name} ! Welcome to my application.')
            print('1 : Details')
            print('2 : Exit')
            option = int(input('Enter you option here :: '))
            while(option>=1 and option < 2):
                print(f'Name :: {self.name}')
                print(f'Name :: {self.age}')    
                print(f'Name :: {self.fname}')
                print(f'Name :: {self.mname}')
                print(f'Name :: {self.gender}')
                print(f'Name :: {self.address}')
                print('Thanks for using this application')
                option=option+1
        except Exception as e:
            print('something went wrong',e) 

rohit = Users('Rohit',24,'Rohan','Mohani','Male','Behra')
rohit.UserInfo()
